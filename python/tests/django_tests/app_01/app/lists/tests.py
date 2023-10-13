from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import home_page 
from .models import Item, List 

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

        response = self.client.post('/lists/new', 
                        data={'item_text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')

# database

class ListAndItemModelTest(TestCase):
    """Django ORM test. Element of list tests."""


    def test_saving_and_retrieving_items(self):

        list_ = List()
        list_.save()

        first_item = Item()
        first_item.list = list_
        first_item.text = 'First item'
        first_item.save()

        second_item = Item()
        second_item.list = list_
        second_item.text = 'Second item'
        second_item.save()

        saved_first = List.objects.first()
        self.assertEqual(saved_first, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0].text
        second_saved_item = saved_items[1].text
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.list, list_)
        self.assertEqual(first_saved_item, 'First item')
        self.assertEqual(second_saved_item, 'Second item')
        



class ListViewTest(TestCase):
    """Test view for list."""

    def test_displays_all_items(self):
        """display all element of list."""

        list_ = List.objects.create()
        Item.objects.create(text='item 1', list=list_)
        Item.objects.create(text='item 2', list=list_)

    def test_uses_list_template(self):
        """use template of list."""

        list_ = List.objects.create()
        response = self.client.get('/lists/unic_list/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        """Display elemts only this list."""

        correct_list = List.objects.create()
        Item.objects.create(text='item 1', list=correct_list)
        Item.objects.create(text='item 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='another element 1 list', list=other_list)
        Item.objects.create(text='another element 2 list', list=other_list)

        response = self.client.get(f'/lists/unic_list/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')
        self.assertNotContains(response, 'another element 1 list')
        self.assertNotContains(response, 'another element 2 list')



class NewListTest(TestCase):
    """NEW LIST"""

    def test_can_save_a_POST_request(self):
        """Test -> save post"""

        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        """redirect after post"""

        response = self.client.post('/lists/new', 
                        data={'item_text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')