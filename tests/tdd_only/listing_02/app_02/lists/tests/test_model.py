from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List

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

    def test_cannot_save_empty_list_items(self):
        """-> dont add empty item""" 

        my_list = List.objects.create()
        item = Item(my_list=my_list, text='')

        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_get_absolute_url(self):
        """-> get sabsolute url"""

        my_list = List.objects.create()
        self.assertEqual(my_list.get_absolute_url(), f'/lists/{my_list.id}/')