import json
import random
import string

from django.http import QueryDict
from django.template.loader import render_to_string
from django.utils import timezone


from registry.registry import ServiceRegistry



def json_super_serializer():
    return None


def validate_email():
    return None



def get_request_data(request):
    try:
        if request is None:
            return QueryDict()

        content_type = request.META.get('CONTENT_TYPE', '')

        if content_type == 'application/json':
            return json.loads(request.body)
        elif content_type.startswith('multipart/form-data'):
            return request.POST.dict()
        elif request.method == 'GET':
            return request.GET.dict()
        elif request.method == 'POST':
            return request.POST.dict()
        else:
            if request.body:
                return json.loads(request.body)
            return QueryDict().dict()
    except json.JSONDecodeError:
        return QueryDict().dict()
    except Exception as e:
        # Log the exception here
        raise ValueError(f"Error parsing request data: {e}")


def get_clean_data(request):
    """
    Cleans the data from the request by explicitly setting all headers to None.
    """
    clean_data = get_request_data(request)

    # Explicitly set each known header to None
    cleaned_headers = {
        "CONTENT_TYPE": None,
        "X-Frame-Options": None,
        "Content-Length": None,
        "Vary": None,
        "X-Content-Type-Options": None,
        "Referrer-Policy": None,
        "Cross-Origin-Opener-Policy": None,
    }

    return clean_data

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))


def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(user):
    otp = generate_otp()

    # Create an OTP session using user_id instead of the user object
    service_registry = ServiceRegistry()
    session = service_registry.database(model_name="UserSession", operation="create", data={
        "user_id": user.id,
        "otp": otp,
        "is_valid": True
    })

    try:
        # Render OTP email template
        html_content = render_to_string('otp_email_template.html', {'otp': otp})

        # Send email using NotificationServiceHandler
        from registry.logbase import TransactionLogBase
        email_service = TransactionLogBase()
        email_service.send_user_email(message=f"Your Verification OTP is {otp}", subject="Verification OTP", to_address=user.email)
        return otp

    except Exception as e:
        from registry.responseprovider import ResponseProvider
        response_provider = ResponseProvider(data={"message": f"error{str(e)}"}, message="Success", code=200)
        return response_provider.exception()

def otp_expired(self):
    is_expired = timezone.now() - self.otp_created_at > timezone.timedelta(hours=8)
    return is_expired

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))