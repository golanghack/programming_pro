from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, get_user_model
from django.contrib.sessions.backends.db import SessionStore
from .base import FunctionalTest

User = get_user_model()

class MyListsTest(FunctionalTest):
    """-> test app 'lists'""" 

    def create_pre_auth_session(self, email):
        """-> create pre authn seans"""

        user = User.objects.create(email=email)
        session = SessionStore()
        session[SESSION_KEY] = user.pk 
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()
        # set cookie for show one domen
        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie(duct(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key, 
            path='/',
        ))