from .base import FunctionalTest
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class NewWisiterTest(FunctionalTest):
    def test_can_start_a_list_for_one_user(self):
        """May by will start a list app and get his later""" 

        self.browser.get(self.live_server_url)
        
        member = 'The install worked'
        container = self.browser.title

        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text 
        self.assertIn('Start To-do list', header_text)

        input_box = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do')

        input_box.send_keys('one')
        input_box.send_keys(Keys.ENTER)
        
        self.wait_for_row_in_list_table('1 -> one')

        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('two')
        input_box.send_keys(Keys.ENTER)
        
        self.wait_for_row_in_list_table('1 -> one')
        self.wait_for_row_in_list_table('2 -> two')
        

    def test_multiple_users_can_start_list_at_different_urls(self):
        """Many users for many urls of lists""" 

        # another user begin new list
        self.browser.get(self.live_server_url)

        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('One from another user')
        input_box.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1 -> One from another user')
        #unic url for list for another user
        another_user_list_url = self.browser.current_url
        self.assertRegex(another_user_list_url, '/lists/.+')

        # exiting and quit for this user
        self.browser.quit()

        # new user
        self.browser = Firefox()
        self.browser.get(self.live_server_url)
        # not seeing before users in browser
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('One from another user', page_text)
        self.assertNotIn('Two', page_text)

        # new list from new user
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('Two from another user')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1 -> Two from another user')
        # nee uniq url for new user
        new_another_user_list_url = self.browser.current_url
        self.assertRegex(new_another_user_list_url, '/lists/.+')
        self.assertNotEqual(new_another_user_list_url, another_user_list_url)
        # not seeing before users in browser
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('One from another user', page_text)
        self.assertIn('Two from another user', page_text)