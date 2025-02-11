from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from jwt import ExpiredSignatureError, decode
from pip._internal.utils import datetime

from Backend import settings
from api.data.data_input import create_user_data
from api.utility.transaction import log_login_transaction
from registry.logbase import TransactionLogBase
from registry.notify import NotificationServiceHandler
from registry.registry import ServiceRegistry
from registry.responseprovider import ResponseProvider
from api.utility.common import get_clean_data, send_otp_email, otp_expired, generate_otp
from api.utility.tokens import issue_tokens
from templates.mail_templates_manager import TemplateManagementEngine


# Create your views here.

@csrf_exempt
def login(request):
    """
    Login view that checks for a valid user session.

    - If username/password are missing or invalid, a 400 is returned.
    - If the user’s session is not active (or the OTP has expired), a new OTP is sent.
    - If a valid session exists, the login transaction is logged and JWT tokens are issued.
    """
    try:
        # Extract and validate request data.
        data = get_clean_data(request)
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return ResponseProvider(
                message="Username and password are required", code=400
            ).bad_request()

        user = authenticate(username=username, password=password)
        if not user:
            return ResponseProvider(
                message="Invalid credentials", code=400
            ).bad_request()

        # Check for an existing active session using your service registry.
        service_registry = ServiceRegistry()
        session = service_registry.database(
            model_name="UserSession",
            operation="filter",
            data={"user": user, "is_valid": True}
        )

        if session:
            # If the session exists but the OTP is expired, mark the session invalid.
            if session is otp_expired:
                service_registry.database(
                    model_name="UserSession",
                    operation="update",
                    instance_id=session.id,
                    data={"is_valid": False}
                )
                session = None

        # If there is no valid session, generate and send a new OTP.
        if not session:
            otp = generate_otp()  # Your OTP generation function.

            # Prepare the replacement values for the template.
            replace_items = {"otp": otp}

            # Instantiate the notification handler (which inherits my template engine).
            notification_handler = NotificationServiceHandler()

            # Generate the email HTML content using the OTP template.
            message = notification_handler.send_login_otp(**replace_items)

            notification_items = [{
                "message_type": "2",
                "destination": user.email,
                "message": message,
                "corporate_id": user.organisation,
            }]

            notification_handler.send_notification(notifications= notification_items)

            # session with the generated OTP.
            service_registry.database("UserSession", "create", data={
                "user": user,
                "otp": otp,
                "is_valid": True
            })

            return ResponseProvider(
                message={"message": "OTP sent to your email"},
                code=200
            ).success()

        return issue_tokens(user)

    except Exception as e:
        return ResponseProvider(message=str(e), code=500).exception()

@csrf_exempt
def create_organization(request):
    try:
        data = get_clean_data(request)
        required_fields = ["name"]

        if TransactionLogBase().has_missing_required_fields(data, required_fields):
            return ResponseProvider(message="Organization name is required", code=400).bad_request()

        organization = ServiceRegistry().database("Organisation", "create", data=data)
        return ResponseProvider(
            data={"organization_id": organization["id"]},
            message="Organization created successfully",
            code=201
        ).success()
    except Exception as e:
        return ResponseProvider(message=f"Error creating organization: {e}", code=500).exception()


@csrf_exempt
def register_user(request):
    try:
        data = get_clean_data(request)
        required_fields = ["username", "password", "email", "role", "organization_id"]

        if TransactionLogBase().has_missing_required_fields(data, required_fields):
            return ResponseProvider(message="All fields are required", code=400).bad_request()

        # Get organization
        organization = ServiceRegistry().database("Organisation", "get", data={"id": data["organization_id"]})
        if not organization:
            return ResponseProvider(message="Organization not found", code=404).bad_request()

        # Create user with hashed password
        user_data = create_user_data(request)
        user = ServiceRegistry().database("User", "create", data=user_data)

        return ResponseProvider(message="User registered successfully", code=201).success()
    except Exception as e:
        return ResponseProvider(message=f"Error registering user: {e}", code=500).exception()


@csrf_exempt
def forgot_password(request):
    try:
        data = get_clean_data(request)
        required_fields = ["username"]

        if TransactionLogBase().has_missing_required_fields(data, required_fields):
            return ResponseProvider(message="Username is required", code=400).bad_request()

        # Get user by username
        users = ServiceRegistry().database("user", "filter", data={"username": data["username"]})
        if not users:
            return ResponseProvider(message="User not found", code=404).bad_request()
        user_id = users[0]["id"]

        # Generate and save OTP
        otp = generate_otp()
        ServiceRegistry().database(
            "forgotpassword",
            "create",
            data={"user": user_id, "otp": otp, "is_valid": True}
        )

        # Send OTP via email (pseudo-implementation)
        # user_email = users[0]["email"]
        # send_email(user_email, "Password Reset OTP", f"Your OTP is {otp}")

        return ResponseProvider(message="OTP sent to email", code=200).success()
    except Exception as e:
        return ResponseProvider(message=f"Error sending OTP: {e}", code=500).exception()


@csrf_exempt
def verify_otp(request):
    try:
        data = get_clean_data(request)
        required_fields = ["username", "otp"]

        if TransactionLogBase().has_missing_required_fields(data, required_fields):
            return ResponseProvider(message="Username and OTP are required", code=400).bad_request()

        # Get user by username
        users = ServiceRegistry().database("user", "filter", data={"username": data["username"]})
        if not users:
            return ResponseProvider(message="User not found", code=404).bad_request()
        user_id = users[0]["id"]

        # Check valid OTP
        otp_entries = ServiceRegistry().database(
            "forgotpassword",
            "filter",
            data={"user": user_id, "otp": data["otp"], "is_valid": True}
        )
        if not otp_entries:
            return ResponseProvider(message="Invalid or expired OTP", code=400).bad_request()

        # Invalidate OTP after verification
        ServiceRegistry().database(
            "forgotpassword",
            "update",
            instance_id=otp_entries[0]["id"],
            data={"is_valid": False}
        )

        return ResponseProvider(message="OTP verified successfully", code=200).success()
    except Exception as e:
        return ResponseProvider(message=f"Error verifying OTP: {e}", code=500).exception()


@csrf_exempt
def reset_password(request):
    try:
        data = get_clean_data(request)
        required_fields = ["username", "otp", "new_password"]

        if TransactionLogBase().has_missing_required_fields(data, required_fields):
            return ResponseProvider(message="Username, OTP, and new password are required", code=400).bad_request()

        # Get user by username
        users = ServiceRegistry().database("user", "filter", data={"username": data["username"]})
        if not users:
            return ResponseProvider(message="User not found", code=404).bad_request()
        user_id = users[0]["id"]

        # Check OTP validity and expiration
        otp_entries = ServiceRegistry().database(
            "forgotpassword",
            "filter",
            data={"user": user_id, "otp": data["otp"], "is_valid": False}
        )
        if not otp_entries:
            return ResponseProvider(message="Invalid OTP or OTP not verified", code=400).bad_request()

        # Check OTP expiration (15 minutes)
        created_at = datetime.fromisoformat(otp_entries[0]["created_at"])
        if (datetime.now() - created_at).total_seconds() > 900:
            return ResponseProvider(message="OTP has expired", code=400).bad_request()

        # Update password using Django ORM for proper hashing
        from django.contrib.auth import get_user_model
        User = get_user_model()
        user = User.objects.get(id=user_id)
        user.set_password(data["new_password"])
        user.save()

        return ResponseProvider(message="Password reset successfully", code=200).success()
    except Exception as e:
        return ResponseProvider(message=f"Error resetting password: {e}", code=500).exception()

@csrf_exempt
def refresh_token_view(request):
    """
    View to refresh JWT tokens.

    This function:
      - Reads the 'refresh_token' cookie.
      - Decodes and validates the refresh token.
      - Checks that the associated user session is still active.
      - If everything is valid, issues new tokens.
      - If the token is expired or the session is inactive, returns an error so that
        the client can force the user to re-authenticate.
    """
    try:
        token = request.COOKIES.get('refresh_token')
        if not token:
            return ResponseProvider(message="Refresh token not provided", code=401).unauthorized()

        # Decode the token. (Ensure that you handle the ExpiredSignatureError.)
        payload = decode(token, settings.JWT_SECRET, algorithms=['HS256'])
        user_id = payload.get('user_id')

        # Retrieve the user (adjust the lookup per your User model).
        from django.contrib.auth.models import User  # or your custom user model
        user = User.objects.get(id=user_id)

        # Check if the user’s session is still active.
        service_registry = ServiceRegistry()
        session = service_registry.database(
            model_name="UserSession",
            operation="filter",
            data={"user": user, "is_valid": True}
        )
        if not session:
            return ResponseProvider(
                message="Session expired. Please re-authenticate.",
                code=403
            ).forbidden()

        # If all is well, issue new tokens.
        return issue_tokens(user)

    except ExpiredSignatureError:
        return ResponseProvider(message="Refresh token expired. Please login again", code=401).unauthorized()
    except Exception as e:
        return ResponseProvider(message=str(e), code=500).server_error()