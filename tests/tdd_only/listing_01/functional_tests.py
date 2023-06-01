import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 
import unittest

class NewTest(unittest.TestCase):
    """Test for New Visiter""" 

    def setUp(self):
        """set"""

        self.browser = Firefox()

    def tearDown(self):
        """Unset""" 

        self.browser.quit() 

    def test_can_start_and_retrieve_it_later(self):
        """May by will start a list app and get his later""" 

        self.browser.get('http://127.0.0.1:8000')
        
        member = 'The install worked'
        container = self.browser.title

        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text 
        self.assertIn('To-do', header_text)

        input_box = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do')

        input_box.send_keys('one')
        input_box.send_keys(Keys.ENTER)
        time.sleep(4)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(any(row.text == '1 -> one' for row in rows))
        self.assertIn(member, container)
        self.fail('ENDED -> ')

if __name__ == '__main__':
    unittest.main()