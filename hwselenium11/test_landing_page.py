import pytest
from selenium import webdriver
import time
from hwselenium11.pageobjects.landing_page import LandingPage




class TestLandingPage:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        yield
        time.sleep(5)
        driver.quit()

    def open_title_page(self, test_setup):
        landing_page=LandingPage(driver)
        landing_page.open()
        assert landing_page.check()

    def test_open_offers(self, test_setup):
        landing_page=LandingPage(driver)
        landing_page.open()
        offers_page=landing_page.open_offers()
        offers_page.choose_service_type("Air conditioning")
        offers_page.choose_service_type("Appliance installation")
        offers_page.choose_state("California")
        offers_page.choose_all_county()
        assert offers_page.check_card_by_title_color("house", "rgb(224, 241, 222)", "R")











