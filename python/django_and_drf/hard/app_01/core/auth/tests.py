import pytest
from rest_framework import status
from core.fixtures.user import user 

class TestAuthViewSet:

    endpoint = '/api/auth/'

    def test_login(self, client, user):
        """-> test login endpoint"""

        data = {
            'username': 'test_10',
            'password': 'test_password'
        }
        response = client.post(self.endpoint + 'login/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']
        assert response.data['user']['id'] == user.public_id.hex
        assert response.data['user']['username'] == user.username
        assert response.data['user']['email'] == user.email

    @pytest.mark.django_db
    def test_register(self, client):
        """-> test register endpoint"""

        data = {
            'username': 'test_11',
            'email': 'test_11@test.com',
            'password': 'test_password',
            'first_name': 'test_11',
            'last_name': 'test_11'
        }
        response = client.post(self.endpoint + 'register/', data)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.db
    def test_refresh(self, client, user):
        """-> test refresh endpoint"""

        data = {
            'username': user.username,
            'password': 'test_password'
        }
        response = client.post(self.endpoint + 'login/', data)
        assert response.status_code == status.HTTP_200_OK

        data = {
            'refresh': response.data['refresh']
        }
        response = client.post(self.endpoint + 'refresh/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']
