
from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets. login import LoginViewSet

router = routers.SimpleRouter()

# auth
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')

# USer
router.register(r'api/user', UserViewSet, basename='user')


urlpatterns = [
    *router.urls,
]