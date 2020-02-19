import pytest
from selenium import webdriver
from Homework.page_objects.landing_page import LandingPage


class TestLandingPage:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/Users/lanapaulikava/PycharmProjects/python_selenium_1/Homework/chromedriver")
        yield
        driver.quit()

    @pytest.mark.skip
    def test_offers(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        offers = landing_page.open_offers()
        offers.choose_service_type("Air conditioning")
        offers.choose_service_type("Appliance installation")
        offers.choose_state("California")
        offers.choose_all_counties()
        assert offers.is_title_exist()
        assert offers.is_status_exist()
        assert offers.is_service_exist()
        assert offers.is_originated_by_exist()
        assert offers.is_r_letter_exist()

