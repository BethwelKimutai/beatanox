import json
import logging
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from os.path import basename

from django.core.validators import validate_email

# from api.interfaces.sms_interface import SMSInterface
from audit.backend.services import NotificationService, NotificationTypeService, TransactionService, TemplateService
from Backend.base.services import OrganisationService
from django.conf import settings
from typing import Dict, Any, List, Optional, Type

from templates.mail_templates_manager import TemplateManagementEngine
# from ussd.backend.services import StateService

log = logging.getLogger(__name__)

class NotificationServiceHandler(TemplateManagementEngine):
    """Handles sending notifications via SMS and Email."""

    def replace_sms_tags(self, session_hop, response_string, **kwargs):
        """Replace tags in the response USSD Page string."""
        try:
            response_string = response_string.replace('[msisdn]', session_hop.msisdn)
            if kwargs is not None:
                for k, v in kwargs.items():
                    response_string = response_string.replace(f'[{k}]', str(v))
            return response_string
        except Exception as e:
            log.exception('%s replace_tags Exception: %s', self.__class__.__name__, e)
        return response_string

    def replace_tags(self, template_string, **kwargs):
        """
        Replaces all the occurrences of replace tags with the passed in arguments.
        @param template_string: The template string we are supposed to replace tags.
        @type template_string: str
        @param kwargs: The key->word arguments representing the tags in the string without []
        @return: The template string replaced accordingly.
        @rtype: str
        """
        try:
            for k, v in kwargs.items():
                template_string = template_string.replace('[%s]' % str(k), str(v))
            return template_string
        except Exception as e:
            log.exception('replace_tags Exception: %s', e)
        return template_string

    # def send_notification(self, notifications: List[Dict[str, Any]], trans=None, attachment=None, cc=None):
    #     """Send notifications through the Notifications Bus."""
    #     if not notifications:
    #         return None
    #     try:
    #         for notification_data in notifications:
    #             message_type = notification_data.get('message_type')
    #             message_code = notification_data.get('message_code', 'LP0008')
    #             organisation_id = notification_data.get('organisation_id')
    #             destination = notification_data.get('destination', '')
    #             replace_tags = notification_data.get('replace_tags', {})
    #             confirmation_code = notification_data.get('confirmation_code', '')
    #
    #             notification_type = NotificationTypeService().get(
    #                 name="SMS" if message_type == '1' else "EMAIL"
    #             )
    #             corporate = OrganisationService().get(id=organisation_id)
    #             template = TemplateService().filter(
    #                 code=message_code, corporate=corporate
    #             )
    #
    #             if template:
    #                 template = template.first()
    #                 custom_message = getattr(template, notification_data.get('lang', ''), '')
    #                 message = self.replace_tags(custom_message, **replace_tags)
    #                 replace_tags['message'] = message
    #             else:
    #                 message = json.dumps(replace_tags, default=json_super_serializer)
    #
    #             notification = NotificationService().create(
    #                 corporate=corporate,
    #                 title=message_code,
    #                 destination=destination,
    #                 message=message,
    #                 state=StateService().get(name="Complete"),
    #                 notification_type=notification_type
    #             )
    #             notification_response = {'code': '400.001.007'}
    #             if notification_type.name == "SMS":
    #                 notification_response = self._send_sms_notification(destination, message, confirmation_code, organisation_id)
    #             else:
    #                 if attachment:
    #                     notification_response = self._send_email_with_attachment(
    #                         destination, message, corporate.name, attachment, cc
    #                     )
    #                 else:
    #                     notification_response = self._send_email_without_attachment(
    #                         destination, message, corporate.name, cc
    #                     )
    #             if notification_response['code'] != '200.001.001':
    #                 NotificationService().update(pk=notification.id, state=StateService().get(name="Failed"))
    #             if trans:
    #                 self._update_transaction_notifications(trans, notification_response)
    #         return 'success'
    #     except Exception as e:
    #         log.exception("send_notification: %s", e)
    #         return None
    #
    # def _send_sms_notification(self, destination, message, confirmation_code, corporate_id):
    #     """Send SMS using Corporates SMS Sender API."""
    #     try:
    #         return SMSInterface().send_sms(destination, message, confirmation_code, corporate_id)
    #     except Exception as e:
    #         log.error("SMS sending failed: %s", e)
    #         return {'code': '400.001.005'}
    #
    def _send_email(self, recipient_email, subject, message, reply_to, cc=None, bcc=None, attachment=None,
                     from_address="jemaerp@gmail.com", sender="jemaerp@gmail.com", password="nmwirqftasmwmits"):
        """Send an email."""
        try:
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['Reply-To'] = reply_to
            msg['To'] = recipient_email
            if cc:
                if not isinstance(cc, list):
                    cc = cc.split(",")
                msg['Cc'] = ",".join(cc)
            if bcc:
                if not isinstance(bcc, list):
                    bcc = bcc.split(",")
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'html'))
            toaddrs = recipient_email.split(",") if isinstance(recipient_email, str) else recipient_email
            if cc:
                toaddrs.extend(cc)
            if bcc:
                toaddrs.extend(bcc)
            if attachment:
                for f in attachment:
                    with open(f, "rb") as fil:
                        part = MIMEApplication(fil.read(), Name=basename(f))
                    part['Content-Disposition'] = f'attachment; filename="{basename(f)}"'
                    msg.attach(part)
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(sender, password)
            server.sendmail(from_address, toaddrs, msg.as_string())
            server.close()
            return {"status": "success", "message": "Email sent successfully"}
        except Exception as e:
            log.error("Error sending email: %s", e)
            return {"status": "failed", "message": f"Error sending email: {e}"}

    def _send_email_with_attachment(self, destination, message, corporate_name, attachment, cc):
        """Send Email with attachment."""
        if not validate_email(destination):
            return {'code': '400.001.005'}
        subject = f"Email Notification - {corporate_name}" or "Dime System"
        try:
            email = self._send_email(
                recipient_email=destination,
                subject=subject,
                message=message,
                reply_to=destination,
                sender="jemaerp@gmail.com",
                attachment=attachment,
                from_address="jemaerp@gmail.com",
                cc=cc,
                password="nmwirqftasmwmits"
            )
            return {'code': '200.001.001'} if email.get('status') == 'success' else {'code': '400.001.007'}
        except Exception as e:
            log.error("Email sending failed: %s", e)
            return {'code': '400.001.007'}

    def _send_email_without_attachment(self, destination, message, corporate_name, cc):
        """Send Email without attachment."""
        if not validate_email(destination):
            return {'code': '400.001.005'}

        subject = f"Email Notification - {corporate_name}" or "Dime System"
        try:
            email = self._send_email(
                recipient_email=destination,
                subject=subject,
                message=message,
                reply_to=destination,
                sender="jemaerp@gmail.com",
                from_address="jemaerp@gmail.com",
                cc=cc,
                password="nmwirqftasmwmits"
            )
            return {'code': '200.001.001'} if email.get('status') == 'success' else {'code': '400.001.007'}
        except Exception as e:
            log.error("Email sending failed: %s", e)
            return {'code': '400.001.007'}

    def _update_transaction_notifications(self, trans, notification_response):
        """Update transaction with notification response."""
        notification_responses = getattr(trans, 'notification_response', None)
        new_response = f"|{notification_response}" if notification_responses else notification_response
        TransactionService().update(trans.id, notification_response=new_response)


