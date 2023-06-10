from .base import FunctionalTest
from unittest import skip

class TestItemValidation(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        """-> not added empty item""" 

        self.fail('Not empty!')