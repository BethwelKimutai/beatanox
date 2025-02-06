from _pydatetime import datetime, timedelta
from jwt import encode
from Backend import settings
from api.responseprovider import ResponseProvider


def handle_token(user):
    try:
        # Generate JWT tokens
        access_payload = {
            'user_id': str(user.id),
            'exp': datetime.utcnow().isoformat(),  # Convert datetime to string
            'iat': datetime.utcnow().isoformat()   # Convert datetime to string
        }
        refresh_payload = {
            'user_id': str(user.id),
            'exp': (datetime.utcnow() + timedelta(days=7)).isoformat(),  # Convert datetime to string
            'iat': datetime.utcnow().isoformat()   # Convert datetime to string
        }

        access_token = encode(access_payload, settings.JWT_SECRET, algorithm='HS256')
        refresh_token = encode(refresh_payload, settings.JWT_SECRET, algorithm='HS256')

        response_provider = ResponseProvider(data={"message": "Login successful"}, message="Success", code=200)
        response = response_provider.success()
        response.set_cookie(
            'access_token',
            access_token,
            httponly=True,
            secure=True,
            samesite='Lax',
            max_age=900  # 15 minutes
        )
        response.set_cookie(
            'refresh_token',
            refresh_token,
            httponly=True,
            secure=True,
            samesite='Lax',
            max_age=604800  # 7 days
        )
        return response
    except Exception as e:
        response_provider = ResponseProvider(message=f"Error creating token: {e}", code=500)
        return response_provider.exception()