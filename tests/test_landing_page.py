import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.common.by import By
import page_objects.landing_page
from page_objects.landing_page import LandingPage
from page_objects.contactor_page import ContractorPage


class TestLandingPage:
    @pytest.fixture()
    def test_setup(self):
        global driver
        global wait

        driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        wait = WebDriverWait(driver,5)
        driver.implicitly_wait(5)

        yield
        time.sleep(5)
        driver.quit()

    # def test_open_title_page(self,test_setup):
    #     landing_page = LandingPage(driver)
    #     landing_page.open()
    #     assert landing_page.check()

    def test_open_contractors(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        contractor_page = landing_page.open_contractor()
        contractor_page.choose_contractor("Air conditioning","California")
        # assert contractor_page.not_fount()

