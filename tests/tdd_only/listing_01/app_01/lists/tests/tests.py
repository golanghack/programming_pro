
from django.test import TestCase
from lists.models import Item, List

class HomeTest(TestCase):
    """Home page test"""

    def test_can_save_a_POST_request(self):
        """-> may save post"""

        pass

class TestListAndItemModel(TestCase):
    """-> model item of list""" 

    def test_saving_and_retrieving_items(self):
        """-> save and get element of list""" 

        my_list = List()
        my_list.save()

        first_item = Item() 
        first_item.my_list = my_list
        first_item.text = 'One'
        first_item.save()

        second_item = Item()
        second_item.text = 'Two'
        second_item.my_list = my_list
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        saved_list = List.objects.first()
        self.assertEqual(saved_list, my_list)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'One')
        self.assertEqual(second_saved_item.text, 'Two')
        self.assertEqual(first_saved_item.my_list, my_list)
        self.assertEqual(second_saved_item.my_list, my_list)



class ListViewTest(TestCase):
    """Testing views of list"""

    def test_uses_list_template(self):
        """Use template for list""" 

        my_list = List.objects.create()
        response = self.client.get(f'/lists/{my_list.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        """Show all elements only this list""" 

        my_list = List.objects.create()
        Item.objects.create(text='item 1', my_list=my_list)
        Item.objects.create(text='item 2', my_list=my_list)

        another_my_list = List.objects.create()
        Item.objects.create(text='another item 1 list', my_list=another_my_list)
        Item.objects.create(text='another item 2 list', my_list=another_my_list)

        response = self.client.get(f'/lists/{my_list.id}/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')

        self.assertNotContains(response, 'another item 1 list')
        self.assertNotContains(response, 'another item 2 list')

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