from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import home_page 
from .models import Item 

class HomePageTest(TestCase):
    """Home page test."""

    def test_uses_base_template(self):
        """Home page with correct html"""

        response = self.client.get('/')
        self.assertTemplateUsed((response, 'base.html'))

    def test_can_save_a_POST_request(self):
        """Test -> can save a post request"""

        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        """Redirecting test."""

        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/unic_list/')

    def test_only_saves_items_when_necessary(self):
        """Only saves elemnts on needs."""

        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


# database
class ItemModelTest(TestCase):
    """Django ORM test. Element of list tests."""

    def test_saving_and_retrieving_items(self):
        """Test saving and take elements of list."""

        first_item = Item()
        first_item.text = 'First item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0].text
        second_saved_item = saved_items[1].text

        self.assertEqual(first_saved_item, 'First item')
        self.assertEqual(second_saved_item, 'Second item')


class ListViewTest(TestCase):
    """Test view for list."""

    def test_uses_list_template(self):
        """use template of list."""

        response = self.client.get('/lists/unic_list/')
        self.assertTemplateUsed(response, 'list.html')