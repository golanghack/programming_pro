from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import math

class TestLayoutStyle(FunctionalTest):
    def test_layout_and_styling(self):
        """-> style"""

        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('test')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1 -> test')

        input_box = self.browser.find_element(By.ID, 'id_new_item')

        self.assertAlmostEqual(math.floor(input_box.location['x'] + input_box.size['width']) / 2, 490, delta=10)

