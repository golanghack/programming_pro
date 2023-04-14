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

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Test
        
        -> may begin list and get his later.
        """

        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').header_text
        self.assertIn('To-Do', header_text)

        input_box = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        input_box.send_keys('Bye wins')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(any(row.text == '1: Bye wins' for row in rows))
        self.fail('End')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    