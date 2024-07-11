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
#     python3 -m pytest -v --driver Chrome --driver-path /tests/chrome test_selenium_petfriends_putest.py
#

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

def test_petfriends(selenium):
    """ Login to PetFriends and make a screenshot of the page. """

    selenium.get("https://petfriends1.herokuapp.com/")

    WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]"))).click()
    WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, u"У меня уже есть аккаунт"))).click()

    field_email = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, "email")))
    field_email.clear()
    field_email.send_keys("isaid.zx@gmail.com")

    field_pass = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, "pass")))
    field_pass.clear()
    field_pass.send_keys("qwerty1234")

    btn_submit = WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    btn_submit.click()

    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(selenium.get_cookies(), cookies)

    selenium.save_screenshot('result_petfriends.png')