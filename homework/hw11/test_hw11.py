import pytest
from selenium import webdriver
import time
from homework.hw11.landing_page11 import LandingPage
from webdriver_manager.chrome import ChromeDriverManager


class TestLandingPage:
    @pytest.fixture()
    def test_setup(self):
        global driver

        # driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = webdriver.Chrome(ChromeDriverManager().install())

        yield
        time.sleep(5)
        driver.quit()

    def test_sign_in_flow(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        sign_in_page = landing_page.open_sign_in()
        sign_in_page.all_sign_in()

    def test_how_it_works(self,test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        how_it_works_page = landing_page.open_how_it_works()
        how_it_works_page.all_how_it_works()

    # @pytest.mark.skip
    def test_blogs(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        blog_page = landing_page.open_blog()
        count_blogs = blog_page.all_blogs()
        assert count_blogs == 12

    def test_hover(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        landing_page.hover()
