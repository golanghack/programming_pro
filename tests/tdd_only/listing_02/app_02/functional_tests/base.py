import os 

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time 


MAX_WAIT = 10 
class FunctionalTest(StaticLiveServerTestCase):
    """-> functional test""" 

    def setUp(self):
        """set"""

        self.browser = Firefox()

    def tearDown(self):
        """Unset""" 

        self.browser.quit() 
    
    def wait(fn):
        """ -> decorator""" 
        def modified_function(*args, **kwargs):
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)
                except (AssertionError, WebDriverException) as err:
                    if time.time() - start_time > MAX_WAIT:
                        raise err 
                    time.sleep(.5)
        return  modified_function
    
    @wait
    def wait_for_row_in_list_table(self, row_text):
        """-> wait string in table"""

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_element(By.TAG_NAME, 'rt')
        self.assertIn(row_text, [row.text for row in rows])

    @wait
    def wait_for(self, member):
        """Waiting string in table of list""" 

        return member()

    @wait
    def wait_to_be_logged_in(self, email):
        """-> wait for log in"""

        self.browser.find_element(By.CLASS_NAME, 'log out')
        navbar = self.browser.find_element(By.CLASS_NAME, 'navbar')
        self.assertIn(email, navbar.text)

    @wait
    def wait_to_be_logged_out(self, email):
        """-> wait for log out""" 

        self.browser.find_element(By.NAME, 'email')
        navbar = self.browser.find_element(By.CLASS_NAME, 'navbar')
        self.assertNotIn(email, navbar.text)
