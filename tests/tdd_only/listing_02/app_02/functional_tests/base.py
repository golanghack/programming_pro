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
    
    def wait_for_row_in_list_table(self, member: str):
        """Waiting string in table of list""" 

        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(member, [row.text for row in rows])
                return 
            except (AssertionError, WebDriverException) as err:
                if time.time() - start_time > MAX_WAIT:
                    raise err 
                time.sleep(0.5)