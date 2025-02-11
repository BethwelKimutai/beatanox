from _pydatetime import datetime, timedelta
from jwt import encode
from Backend import settings
from registry.responseprovider import ResponseProvider


def issue_tokens(user):
    """
    Generates a new access token (valid for 15 minutes) and refresh token (valid for 7 days),
    then sets them in secure HTTP-only cookies.

    Note: The JWT 'exp' claim is set as a Unix timestamp.
    """
    try:
        access_exp = datetime.utcnow() + timedelta(minutes=15)
        refresh_exp = datetime.utcnow() + timedelta(days=7)
        access_payload = {
            'user_id': str(user.id),
            'exp': access_exp.timestamp(),
            'iat': datetime.utcnow().timestamp()
        }
        refresh_payload = {
            'user_id': str(user.id),
            'exp': refresh_exp.timestamp(),
            'iat': datetime.utcnow().timestamp()
        }

        access_token = encode(access_payload, settings.JWT_SECRET, algorithm='HS256')
        refresh_token = encode(refresh_payload, settings.JWT_SECRET, algorithm='HS256')

        response_provider = ResponseProvider(
            data={"message": "Login successful"}, message="Success", code=200
        )
        response = response_provider.success()
        response.set_cookie(
            'access_token',
            access_token,
            httponly=True,
            secure=True,
            samesite='Lax',
            max_age=900  # 15 minutes in seconds.
        )
        response.set_cookie(
            'refresh_token',
            refresh_token,
            httponly=True,
            secure=True,
            samesite='Lax',
            max_age=604800  # 7 days in seconds.
        )
        return response
    except Exception as e:
        return ResponseProvider(message=f"Error creating token: {e}", code=500).exception()


