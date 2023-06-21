
from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet

router = routers.SimpleRouter()
# USer
router.register(r'api/user', UserViewSet, basename='user')
router.register(r'api/auth/register', RegisterViewSet, basename='auth-register')

urlpatterns = [
    *router.urls,
]