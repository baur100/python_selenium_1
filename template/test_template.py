import pytest
from selenium import webdriver
import time
from SDGE.landing_page_sdge import LandingPage
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture() are functions, which will run before each test function to which it is applied. Fixtures are used
# to feed some data to the tests such as database connections, URLs to test and some sort of input data

class TestLandingPage:
    @pytest.fixture()
    def test_setup(self):
        global driver

        # driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # this is time wait before driver quite (browser close)

        yield
        time.sleep(15)
        driver.quit()

    def test_sign_in_flow(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        landing_page.all_sign_in()
        text = landing_page.text()
        assert text == '$26.96'