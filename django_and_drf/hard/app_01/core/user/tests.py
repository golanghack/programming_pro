import pytest
from core.user.models import User

data_user = {
    'username': 'test_user',
    'email': 'test_10@test.com',
    'first_name': 'Test',
    'last_name': 'User',
    'password': 'test_password',
}

@pytest.mark.django_db
def test_create_user():
    """-> test create user from test data""" 

    user = User.objects.create(**data_user)
    assert user.username == data_user['username']
    assert user.email == data_user['email']
    assert user.first_name == data_user['first_name']
    assert user.last_name == data_user['last_name']

