import unittest
from django.test import LiveServerTestCase
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 

class TestNewVisiter(LiveServerTestCase):
    """Test for New Visiter""" 

    def setUp(self):
        """set"""

        self.browser = Firefox()

    def tearDown(self):
        """Unset""" 

        self.browser.quit() 
    
    def check_for_row_in_list_table(self, member: str):
        """String in table of list""" 

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        container = [row.text for row in rows]

        self.assertIn(member, container)

    def test_can_start_and_retrieve_it_later(self):
        """May by will start a list app and get his later""" 

        self.browser.get(self.live_server_url)
        
        member = 'The install worked'
        container = self.browser.title

        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text 
        self.assertIn('To-do', header_text)

        input_box = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do')

        input_box.send_keys('one')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1 -> one')

        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('two')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1 -> one')
        self.check_for_row_in_list_table('2 -> two')
        
