from django.test import TestCase
from lists.forms import ItemForm

class ItemFormTest(TestCase):
    """-> form test for element of list"""

    def test_form_renders_item_text_input(self):
        """-> form show text input"""

        form = ItemForm()
        self.fail(form.as_p())