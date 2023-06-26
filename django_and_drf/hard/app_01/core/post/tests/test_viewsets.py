from rest_framework import status
from core.fixtures.user import user
from core.fixtures.post import post
import pytest

class TestPostViewSet:
    endpoint = '/post/'

    def test_list(self, client, user, post):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_retrieve(self, client, user, post):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(post.public_id) + '/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == post.public_id.hex
        assert response.data['body'] == post.body
        assert response.data['author']['id'] == post.author.public_id.hex

    def test_create(self, client, user):
        client.force_authenticate(user=user)
        data = {
            'body': 'Test',
            'author': user.public_id.hex
        }
        response = client.post(self.endpoint, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['body'] == data['body']
        assert response.data['author']['id'] == user.public_id.hex


    def test_update(self, client, user, post):
        client.force_authenticate(user=user)
        data = {
            'body': 'Test',
            'author': user.public_id.hex
        }

        response = client.put(self.endpoint + str(post.public_id) +'/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['body'] == data['body']

    def test_delete(self, client, user, post):
        client.force_authenticate(user=user)
         
        response = client.delete(self.endpoint + str(post.public_id) + '/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
    

    def test_list_anonymous(self, client, post):
        response = client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
    
    def test_retrieve_anonymouse(self, client, post):
        response = client.get(self.endpoint + str(post.public_id) + '/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == post.public_id.hex
        assert response.data['body'] == post.body
        assert response.dat['author']['id'] == post.author.public_id.hex

    def test_create_anonymouse(self, client):
        data = {
            'body': 'Test',
            'author': 'test_user'
        }
        response = client.post(self.endpoint, data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_anonymouse(self, client, post):
        data = {
            'body': 'Test',
            'author': 'test_user'
        }

        response = client.put(self.endpoint + str(post.public_id) + '/', data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_anonymouse(self, client, post):
        response = client.delete(self.endpoint + str(post.public_id) + '/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

