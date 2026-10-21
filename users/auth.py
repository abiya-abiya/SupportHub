import jwt
from django.contrib.auth.models import AbstractUser
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

from users.models import User

class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None
        try:
            prefix, token = auth_header.split(' ')
            if prefix.lower() != 'bearer':
                return None
        except ValueError:
            return None

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user_id = payload.get('user_id')
            user = User.objects.get(id=user_id)
            return (user, None)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT token has expired')
        except (jwt.DecodeError, jwt.InvalidTokenError):
            raise AuthenticationFailed('Invalid token')

