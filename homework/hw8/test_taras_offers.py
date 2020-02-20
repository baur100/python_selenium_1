# from selenium import webdriver
# import time
# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# # Homework 1============================================
#
# class Test_Offers:
#     @pytest.fixture()
#     def test_setup(self):
#         global driver
#         driver = webdriver.Chrome(executable_path="./chromedriver")
#         driver.implicitly_wait(6)
#         driver.maximize_window()
#         driver.get("https://testkwidos.tk/")
#         yield
#         time.sleep(3)
#         driver.quit()
#
#         # HOMEWORK 1.1
#
#     def test_homework_1_1(self, test_setup):
#
#         offers = driver.find_element_by_xpath("//*[contains(text(), 'OFFERS')]")
#         offers.click()
#
#         service_type = driver.find_element_by_css_selector(".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")
#         service_type.click()
#
#         select = driver.find_element_by_xpath("//label[contains(text(),'Air conditioning')]")
#         select.click()
#
#         close = driver.find_element_by_css_selector(".pi.pi-times")
#         close.click()
#
#         state_field = driver.find_element_by_css_selector(".ui-dropdown-trigger-icon.ui-clickable.pi.pi-caret-down")
#         state_field.click()
#
#         california = driver.find_element_by_xpath("//span[contains(text(),'California')]")
#         california.click()
#
#         text = driver.find_element_by_xpath("//*[contains(text(), 'house')]").text
#         assert "house" == text
#
#     # HOMEWORK 1.2
#
#     def test_homework_1_2(self, test_setup):
#         offers = driver.find_element_by_xpath("//*[text()='OFFERS']")
#         offers.click()
#
#         service_type = driver.find_element_by_css_selector(".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")
#         service_type.click()
#
#         select = driver.find_element_by_xpath("//label[contains(text(),'Air conditioning')]")
#         select.click()
#
#         close = driver.find_element_by_css_selector(".pi.pi-times")
#         close.click()
#
#         state_field = driver.find_element_by_css_selector(".ui-dropdown-trigger-icon.ui-clickable.pi.pi-caret-down")
#         state_field.click()
#
#         iterate_state = driver.find_elements_by_xpath("//div[@class='ui-dropdown-items-wrapper']/ul/li/span")
#         for wyo in iterate_state:
#             if wyo.text == "Wyoming":
#                 wyo.click()
#
#     def test_homework_1_3(self, test_setup):
#         blog = driver.find_element_by_xpath("//p[contains(text(),'BLOG')]")
#         blog.click()
#
#         scroll_down = driver.find_element_by_xpath("//span[contains(text(),'Kwidos is the place for new businesses')]")
#         driver.execute_script("arguments[0].scrollIntoView();", scroll_down)
