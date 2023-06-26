import pytest
from core.fixtures.user import user as user
from core.post.models import Post

@pytest.mark.django_db
def test_create_post(user):
    """-> create post with test user"""

    post = Post.objects.create(author=user, body='Test')
    assert post.body == 'Test'
    assert post.author == user

    