
from django.test import TestCase
from lists.models import Item 

class HomeTest(TestCase):
    """Home page test"""

    def test_can_save_a_POST_request(self):
        """-> may save post"""

        pass

class TestModelItem(TestCase):
    """-> model item of list""" 

    def test_saving_and_retrieving_items(self):
        """-> save and get element of list""" 

        first_item = Item() 
        first_item.text = 'One'
        first_item.save()

        second_item = Item()
        second_item.text = 'Two'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'One')
        self.assertEqual(second_saved_item.text, 'Two')



class ListViewTest(TestCase):
    """Testing views of list"""

    def test_displays_all_list_items(self):
        """Show all elements of list""" 

        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/lists/one/')
        
        member_one = 'item 1'
        member_two = 'item 2'
        
        self.assertContains(response, member_one)
        self.assertContains(response, member_two)

    def tests_uses_list_template(self):
        """-> use template of list""" 

        response = self.client.get('/lists/one/')
        self.assertTemplateUsed(response, 'list.html')


class NewListTest(TestCase):
    """-> new list""" 

    def test_can_save_a_POST_request(self):
        """-> may save post"""

        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        """-> redirect after POST""" 

        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/one/')