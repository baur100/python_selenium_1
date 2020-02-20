# import pytest
# from selenium import webdriver
# import time
# from homework.hw10.landing_page_county import LandingPage
# from homework.hw10.contractors_county import ContractorPage
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class TestLandingPage:
#     @pytest.fixture()
#     def test_setup(self):
#         global driver
#
#         # driver = webdriver.Chrome(executable_path="./chromedriver")
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#
#
#         yield
#         time.sleep(5)
#         driver.quit()
#
#     def test_open_contractors(self, test_setup):
#         landing_page = LandingPage(driver)
#         landing_page.open()
#         contractor_page = landing_page.open_contractor()
#         contractor_page.choose_contractor("Air conditioning", "Appliance installation", "California", "Orange")
#         assert contractor_page.is_not_found_message()
