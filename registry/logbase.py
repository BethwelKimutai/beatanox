import logging
from typing import Dict, Any, List, Optional
from django.db import transaction

from .notify import NotificationServiceHandler
from registry.responseprovider import ResponseProvider
from Authentication.models import Transaction
from api.utility.common import get_request_data
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
logger = logging.getLogger(__name__)


class TransactionLogBase(ResponseProvider, NotificationServiceHandler):
	"""Class for logging transactions."""



	def complete_transaction(self, transaction_obj: Transaction, **kwargs: Any) -> Optional[Transaction]:
		"""
		Marks the transaction object as complete.
		"""
		try:
			kwargs.setdefault('state', self.registry.database('state', 'get', data={"name": "Completed"}))
			# notifications = kwargs.pop('notification_details', [])
			# Thread(target=self._send_notification, args=(notifications, transaction_obj)).start()
			return self.registry.database('transaction', 'update', instance_id=transaction_obj.id, data=kwargs)
		except Exception as e:
			logger.exception('Exception in complete_transaction: %s', e)
		return None

	def log_transaction(self, transaction_type: str, **kwargs: Any) -> Optional[Transaction]:
		"""
		Logs a transaction of the given type with the provided arguments.
		"""
		try:
			with transaction.atomic():
				self.registry.database('state', 'get', data={"name": "Active"})
				transaction_type_instance = self.registry.database('transactiontype', 'get', data={"name": transaction_type})
				kwargs.setdefault('state', self.registry.database('state', 'get', data={"name": "Active"}))

				request = kwargs.pop('request', None)
				if request:
					kwargs['euser'] = getattr(request, 'euser', None)
					data = get_request_data(request)
					if data:
						kwargs['source_ip'] = data.get('source_ip')
						kwargs['request'] = data
				if 'bulk_request' in kwargs:
					kwargs['request'] = kwargs.pop('bulk_request')
					kwargs['bulk'] = True

				kwargs['transaction_type'] = transaction_type_instance
				return self.registry.database('transaction', 'create', data=kwargs)
		except Exception as e:
			logger.exception('Exception in log_transaction: %s', e)
		return None

	def mark_transaction_failed(self, transaction_obj: Transaction, **kwargs: Any) -> Optional[Transaction]:
		"""
		Marks the transaction object as failed.
		"""
		try:
			kwargs.setdefault('state', self.registry.database('state', 'get', data={"name": "Failed"}))
			# notifications = kwargs.pop('notification_details', [])
			# Thread(target=self._send_notification, args=(notifications, transaction_obj)).start()
			return self.registry.database('transaction', 'update', instance_id=transaction_obj.id, data=kwargs)
		except Exception as e:
			logger.exception('Exception in mark_transaction_failed: %s', e)
		return None

	def has_missing_required_fields(self, data: Dict[str, Any], required_fields: List[str]) -> bool:
		"""
		Checks if there are missing required fields in the given data.

		:param data: The dictionary containing the data to check.
		:param required_fields: A list of fields that must be present in the data.
		:return: True if there are missing required fields, False otherwise.
		"""
		missing_fields = [field for field in required_fields if not data.get(field)]
		if missing_fields:
			logger.info("Missing fields: %s", missing_fields)
			logger.info("Data provided: %s", data)
			return True
		return False



	def send_user_email(self, message, subject, to_address):
		"""
		"""
		from_address = "jemaerp@gmail.com"
		msg = MIMEMultipart()
		msg['From'] = from_address
		# msg['Reply-To'] = reply_to
		msg['To'] = to_address
		msg['Date'] = formatdate(localtime=True)
		msg['Subject'] = subject

		msg.attach(MIMEText(message, 'html'))
		toaddrs = [to_address]
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login("jemaerp@gmail.com", "nmwirqftasmwmits")
		server.set_debuglevel(0)
		server.sendmail(msg['To'], toaddrs, msg.as_string())
		server.close()
		return {"status": "success", "message": "Email sent successfully"}

	def process_failed_transaction(self, transaction, message, response):
		if transaction:
			self.mark_transaction_failed(transaction, message=message, response=response)
		return ResponseProvider(code=response, message=message).exception()

	def process_successful_transaction(self, transaction, message):
		if transaction:
			self.complete_transaction(transaction, message=message, response='200.000.000')
		return ResponseProvider(data={"code": "200.000.000", "data": message}).success()

	def create_http_request(self, data):
		"""
		Create an HttpRequest object and set its attributes based on a given dictionary.

		Args:
		- data (dict): A dictionary where keys are attribute names and values are attribute values.

		Returns:
		- request (HttpRequest): The HttpRequest object with the attributes set.
		"""
		from django.http import HttpRequest

		request = HttpRequest()
		for key, value in data.items():
			setattr(request, key, value)

		return request
