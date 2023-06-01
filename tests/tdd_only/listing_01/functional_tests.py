import unittest
from selenium.webdriver import Firefox

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
        self.assertIn(member, container)
        self.fail('ENDED -> ')

if __name__ == '__main__':
    unittest.main(warnings='ignore')