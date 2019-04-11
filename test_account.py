from django.test import TestCase
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class tests_account(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "admin"
        pwd = "password123"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://rentadev.pythonanywhere.com")
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[3]/a')
        #elem = driver.find_element_by_class_name('glyphicon-log-in')
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(user)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(pwd)
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/form/button')
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/ul/li[3]/a').click()
        #driver.get("http://rentadev.pythonanywhere.com/profile")
        time.sleep(1)
        elem = driver.find_element_by_class_name('btn-lg')
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_name('first_name')
        elem.send_keys('Admin')
        elem = driver.find_element_by_name('last_name')
        elem.send_keys('Admin')
        elem = driver.find_element_by_name('email')
        #elem.clear()
        elem.send_keys('Admin@admin.com')
        elem = driver.find_element_by_name('password')
        elem.send_keys('password123')
        elem = driver.find_element_by_name('password2')
        elem.send_keys('password123')
        elem = driver.find_element_by_class_name('btn-lg')
        elem.click()
        time.sleep(2)
        assert "profile edited"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

# Create your tests here.
