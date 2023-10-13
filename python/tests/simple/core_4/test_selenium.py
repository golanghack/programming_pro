#! /usr/bin/env python3 

import selenium

def test_visit_site_of_pytest(selenium=selenium):
    selenium.get('https://docs.pytest.org/en/latest/')
    
    assert 'helps you write better programs' in selenium.title 
    
    element = selenium.find_element_by_link_text('Contents')
    element.click()
    
    assert 'Full pytest docs' in selenium.title 