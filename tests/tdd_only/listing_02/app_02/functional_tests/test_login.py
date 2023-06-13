from django.core import mail 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
from functional_tests.base import FunctionalTest

TEST_EMAIL = 'testOne@example.com'
SUBJECT = 'Your login link for lists'

class LoginTest(FunctionalTest):
    """-> test auth in system"""

    def test_can_get_email_link_to_log_in(self):
        """-> email to link"""

        self.browser.get(self.live_server_url)
        self.browser.find_element(By.NAME, 'email').send_keys(TEST_EMAIL)
        self.browser.find_element(By.NAME, 'email').send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertIn('Check your email', self.browser.find_element(By.TAG_NAME, 'body').text))

        email = mail.outbox[0]
        self.assertIn(TEST_EMAIL, email.to)
        self.assertEqual(email.subject, SUBJECT)
        self.assertIn('Use this link to log-in -> ', email.body)
        url_search = re.search(r'http://.+/.+$', email.body)
        if not url_search:
            self.fail(f'Could not find url in email body -> \n{email.body}')
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        