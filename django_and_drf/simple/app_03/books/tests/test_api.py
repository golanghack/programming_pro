from django.test import TestCase
from ..models import Contact
from django.urls import reverse
from django.forms.models import model_to_dict

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

       