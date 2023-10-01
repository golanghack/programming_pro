import pytest
from core.fixtures.user import user
from core.post.models import Post

@pytest.mark.django_db 
def test_create_post(user):
    """Test create post""" 

    post = Post.objects.create(author=user, body='Test')

    assert post.body == 'Test'
    assert post.author == user
    
