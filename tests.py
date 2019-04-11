from django.test import TestCase
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "admin"
        pwd = "password123"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://rentadev.pythonanywhere.com")
        time.sleep(2)
        elem = driver.find_element_by_class_name('glyphicon-log-in')
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(user)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(pwd)
        time.sleep(2)
        elem = driver.find_element_by_class_name('btn-lg')
        elem.click()
        time.sleep(2)
        assert "Logged In"
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

# Create your tests here.
