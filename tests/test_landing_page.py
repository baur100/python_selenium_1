import pytest
from selenium import webdriver
import time
from page_objects.landing_page import LandingPage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options



class TestLandingPage:
    @pytest.fixture()
    def test_setup(self):
        global driver
        options = Options()
        options.headless=True
        options.add_argument('window-size=1980,1080')
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_options=options)
        driver = webdriver.Chrome(options=options,executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(5)

        yield
        time.sleep(5)
        driver.quit()

    @pytest.mark.ac_test
    def test_open_contractors_arizaona(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        contractor_page = landing_page.open_contractor()
        contractor_page.choose_contractor("Air conditioning", "Arizona")
        assert contractor_page.is_not_found_message()
    # @pytest.mark.skip
    @pytest.mark.xfail
    def test_open_contractors_california_failed(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        contractor_page = landing_page.open_contractor()
        contractor_page.choose_contractor("Air conditioning", "California")
        assert contractor_page.is_not_found_message()

    def test_open_contractors_california_passed(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        contractor_page = landing_page.open_contractor()
        contractor_page.choose_contractor("Air conditioning", "California")
        assert contractor_page.contractor_is_exist("Handalf")

    @pytest.mark.ac_test
    def test_open_contractors_alabama_3d_passed(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        contractor_page = landing_page.open_contractor()
        contractor_page.choose_contractor("3D Capture", "Alabama")
        assert contractor_page.contractor_is_exist("Phil C Inc.")

    @pytest.mark.parametrize("service, state, name",[("Air conditioning", "California", "Handalf"),("3D Capture", "Alabama", "Phil C Inc.")])
    def test_parametrized(self, test_setup, service,state,name):
        landing_page = LandingPage(driver)
        landing_page.open()
        contractor_page = landing_page.open_contractor()
        contractor_page.choose_contractor(service, state)
        assert contractor_page.contractor_is_exist(name)