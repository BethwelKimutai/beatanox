from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Authentication.models import UserSession
from api.notify import NotificationServiceHandler
from api.registry import ServiceRegistry
from api.responseprovider import ResponseProvider
from api.utility.common import get_clean_data, send_otp_email, otp_expired
from api.utility.tokens import handle_token


# Create your views here.

@csrf_exempt
def login(request):
    try:
        data = get_clean_data(request)
        username = data.get("username")
        password = data.get("password")

        if not username or not password:  # Ensure both username and password are provided
            response_provider = ResponseProvider(message="Username and password are required", code=400)
            return response_provider.bad_request()

        user = authenticate(username=username, password=password)
        if not user:
            response_provider = ResponseProvider(message="Invalid credentials", code=400)
            return response_provider.bad_request()

        service_registry = ServiceRegistry()
        session = service_registry.database(model_name="UserSession", operation="filter",
                                            data={"user": user, "is_valid": True})

        if session:
            if session is otp_expired:
                service_registry.database(model_name="UserSession", operation="update", instance_id=session.id,
                                          data={"is_valid": False})
                session = None

        if not session:
            send_otp_email(user)
            response_provider = ResponseProvider(data={"message": "Login successful"}, message="Success", code=200)
            return response_provider.success()

        return handle_token(user)

    except Exception as e:
        response_provider = ResponseProvider(message=f"Error sending OTP email: {e}", code=500)
        return response_provider.exception()

