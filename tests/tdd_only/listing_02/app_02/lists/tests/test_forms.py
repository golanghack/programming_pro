from django.test import TestCase
from lists.forms import ItemForm

class ItemFormTest(TestCase):
    """-> form test for element of list"""

    def test_form_renders_item_text_input(self):
        """-> form show text input"""

        form = ItemForm()
        self.fail(form.as_p())

    def test_form_item_input_has_placeholder_and_css_classes(self):
        """-> field input have attr placeholder and css clsses"""

        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())