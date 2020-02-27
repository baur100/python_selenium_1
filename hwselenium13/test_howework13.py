import pytest
from selenium import webdriver
import time
from hwselenium13.pageobjects.landing_page import LandingPage

class TestHomeWork13:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        yield
        time.sleep(5)
        driver.quit()

    def test_open_reg_page(self, test_setup):
        landing_page=LandingPage(driver)
        landing_page.open()
        reg_page=landing_page.open_register_consumer()
        reg_page.check_in()
        reg_page.fill_out_form("Julya", "Jones", "(818) 222-1111", "JulyaJones22@gmail.com", "JulyaJones222&")
        reg_page.click_button()
        assert reg_page.accountExists('User already exists')

    def test_count_messages_blog(self, test_setup):
        landing_page=LandingPage(driver)
        landing_page.open()
        blog_page=landing_page.open_blog()
        assert blog_page.count_blog() == 12

    def test_How_it_works_screenshot(self, test_setup):
        landing_page=LandingPage(driver)
        landing_page.open()
        how_it_works=landing_page.open_how_it_works()
        how_it_works.take_screenshot("ScreenShot.png")

    def test_mouse_hover(self, test_setup):
        landing_page=LandingPage(driver)
        landing_page.open()
        #landing_page.mouse_hover()
        assert landing_page.is_hovered()













    # def open_offers(self, test_setup):
    #     landing_page=LandingPage(driver)
    #     landing_page.open()
        #offers_page=landing_page.open_offers()
        # offers_page.choose_service_type("Air conditioning")
        # offers_page.choose_service_type("Appliance installation")
        # offers_page.choose_state("California")
        # offers_page.choose_all_county()
        # assert offers_page.check_card_by_title_color("house", "rgb(224, 241, 222)", "R")
