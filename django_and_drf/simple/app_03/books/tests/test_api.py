from django.test import TestCase
from ..models import Contact
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

class TestContanctForm(TestCase):

    def test_can_send_message(self):

        data = {
            'first_name': 'Joe', 
            'last_name': 'Dow', 
            'message': 'Hello Joe',
        }

        contact = Contact.objects.create(
            first_name='Jane', 
            last_name='Dow', 
            message='Hello, Jane',
        )

        self.assertEqual(str(contact), 'Jane Dow')
        data = model_to_dict(contact)
        response = self.client.post(reverse('contact'), data=data)
        self.assertRedirects(response, reverse('correct'))


class TestDownloadView(TestCase):

    def test_anonymous_cannot_see_page(self):
        response = self.client.get(reverse('download'))
        self.assertRedirects(response, '/accounts/login/?next=/download/')

    def test_authenticated_user_cn_see_page(self):
        user = User.objects.create_user('Ben', 'ben@ben.com', 'pass')
        self.client.force_login(user=user)
        response = self.client.get(reverse('download'))
        self.assertEqual(response.status_code, 200)