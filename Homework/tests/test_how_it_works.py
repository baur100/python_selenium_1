import pytest
from selenium import webdriver
from Homework.page_objects.landing_page import LandingPage


class TestHowItWorks:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/Users/lanapaulikava/PycharmProjects/python_selenium_1/Homework/chromedriver")
        yield
        driver.quit()

    @pytest.mark.skip
    def test_open_close_screenshot(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        how_it_works = landing_page.open_how_it_works()
        how_it_works.open_screenshot()
        how_it_works.close_screenshot()

  