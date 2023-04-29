from django.test import TestCase
from ..models import Contact
from django.urls import reverse


class TestContanctForm(TestCase):

    def test_can_send_message(self):

        data = {
            'first_name': 'Joe', 
            'last_name': 'Dow', 
            'message': 'Hello Joe',
        }

        contact = Contact.objects.create()
        rsponse = self.client.get(reverse('contact'))
        # created Contaxct in db?
        response = self.client.post('/contact/', data=data)
        self.assertEqual(Contact.objects.count(), 2)

        # correct redirect?
        self.assertRedirects(response, '/correct/')

       