import pytest
from selenium import webdriver
from Homework.page_objects.landing_page import LandingPage


class TestLandingMenu:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/Users/lanapaulikava/PycharmProjects/python_selenium_1/Homework/chromedriver")
        yield
        driver.quit()

    def test_hover_over_menu(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        landing_page.hover()


