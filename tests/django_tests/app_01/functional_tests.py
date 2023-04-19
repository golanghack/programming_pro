#! /usr/bin/env python3 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """Test of new user."""

    def setUp(self):
        """Setting."""

        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Remove."""

        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """Checking string in table of list."""

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Test-> may begin list and get his later.
        """
        
        self.browser.get('http://localhost:8000')
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('Bye wins')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Bye wins')

        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('Make auto')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Bye wins')
        self.check_for_row_in_list_table('2: Make auto')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
    