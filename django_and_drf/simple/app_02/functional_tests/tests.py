#! /usr/bin/env python3 

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By 

class NewVisitorTest(LiveServerTestCase):
    """Test of new user."""

    def setUp(self):
        """Setting."""

        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        """Remove."""

        self.browser.quit()

    def test_body_test(self):

        body = self.browser.title
        text = 'The install worked'
        self.assertIn(text, body)
        