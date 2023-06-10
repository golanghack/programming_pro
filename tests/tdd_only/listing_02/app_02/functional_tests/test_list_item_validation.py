from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestItemValidation(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        """-> not added empty item""" 

        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text, 
            'List item dont empty!')
            )
        
        self.browser.find_element(By.ID, 'id_new_item').send_keys('One')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1 -> One')

        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has_error').text,
            'List item dont empty!'
        ))

        self.browser.find_element(By.ID, 'id_new_item').send_keys('Two')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1 -> One')
        self.wait_for_row_in_list_table('2 -> Two')