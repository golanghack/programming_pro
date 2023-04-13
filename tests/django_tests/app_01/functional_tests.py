#! /usr/bin/env python3 

from selenium import webdriver

browser = webdriver.Firefox()

# Bob listen about cool app
# and open browser in localhost:8000
browser.get('http://localhost:8000')

# Bob see title of site 
assert 'To-Do' in browser.title

browser.quit()