#! /usr/bin/env python3

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """Test of new user."""

    def setUp(self):
        """Setting."""

        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Remove."""

        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Test

        -> may begin list and get his later.
        """

        self.browser.get("http://localhost:8000/blog")
        self.assertIn("My blog", self.browser.title)


if __name__ == "__main__":
    unittest.main(warnings="ignore")
