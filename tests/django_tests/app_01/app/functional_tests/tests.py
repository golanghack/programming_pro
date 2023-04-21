#! /usr/bin/env python3 

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import WebDriverException
import time
import unittest

MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):
    """Test of new user."""

    def setUp(self):
        """Setting."""

        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Remove."""

        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        """Checking string in table of list."""

        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as err:
                if time.time() - start_time > MAX_WAIT:
                    raise err 
                time.sleep(.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Test-> may begin list and get his later.
        """
        
        self.browser.get(self.live_server_url)
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('Bye wins')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Bye wins')

        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('Make auto')
        input_box.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Bye wins')
        self.wait_for_row_in_list_table('2: Make auto')

    