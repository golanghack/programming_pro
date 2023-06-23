from rest_framework_nested import nested_routers
from rest_framework.routers import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet
from core.post.viewsets import PostViewSet
from core.comment.viewsets import CommentViewSet

router = routers.SimpleRouter()

# auth
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USer
router.register(r'api/user', UserViewSet, basename='user')

# Post
router.register(r'api/post', PostViewSet, basename='post')
post_router = nested_routers.NestedSimpleRouter(router, r'post', lookup='post')
post_router.register(r'comment', CommentViewSet, basename='post-comment')

urlpatterns = [
    *router.urls,
    *post_router.urls,
]