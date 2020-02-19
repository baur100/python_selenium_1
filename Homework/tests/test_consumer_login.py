import pytest
from selenium import webdriver
from Homework.page_objects.landing_page import LandingPage
from Homework.page_objects.consumer import Consumer

import time

class TestLogin:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/Users/lanapaulikava/PycharmProjects/python_selenium_1/Homework/chromedriver")

        yield
        driver.quit()

    @pytest.mark.skip
    def test_consumer_login(self, test_setup):
        landing_page = LandingPage(driver)
        consumer = Consumer('Test', 'Testlp', '9999999999', 'lana.test1@yahoo.com', 'new@20passworD')
        landing_page.open()
        sign_in = landing_page.open_sign_in()
        sign_in.login(consumer.email, consumer.password, consumer.first_name, consumer.last_name)
        time.sleep(5)