#!/usr/bin/python3
# -*- encoding=utf8 -*-

# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download gecko driver for Chrome here:
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path /tests/chrome test_selenium_simple.py
#

import time
import pytest

def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    selenium.get('https://google.com')

    search_input = selenium.find_element_by_name('q')
    search_input.clear()
    search_input.send_keys('first test')

    search_button = selenium.find_element_by_name("btnK")
    search_button.click()

    selenium.save_screenshot('result.png')