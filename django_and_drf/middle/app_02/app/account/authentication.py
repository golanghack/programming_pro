from django.contrib.auth.models import User
from .models import Profile


class EmailAuthBackend:

    def authenticate(self, request: str, username: str=None, password: str=None):
        """Return user or None
        
        from db get user with this email and testing with check_password
        get user from db for id -> primary key(pk)
        """

        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

        def get_user(self, user_id):

            try:
                return User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return None

def create_profile(backend, user, *args, **kwargs):
    """Create profile user for social auth"""

    Profile.objects.get_or_create(user=user)