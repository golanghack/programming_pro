import sys
from accounts.models import ListUser, Token

class PasswordLessAuthenticationBackend(object):
    """-> server process without password authenticated"""

    def authenticate(self, uid):
        """-> auth"""

        print('uid', uid, file=sys.stderr)
        if not Token.objects.filter(uid=uid).exists():
            print('no token found', file=sys.stderr)
            return None
        token = Token.objects.get(uid=uid)
        print('got token', file=sys.stderr)
        try:
            user = ListUser.objects.get(email=token.email)
            print('got user', file=sys.stderr)
            return user 
        except ListUser.DoesNotExist:
            print('new user', file=sys.stderr)
            return ListUser.objects.create(email=token.email)
    
    def get_user(self, email):
        """-> get user""" 

        return ListUser.objects.get(email=email)