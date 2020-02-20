# from homework.hw11.base_page11 import BasePage
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
# import time
#
#
# class HowItWorksPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     @property
#     def first_title(self):
#         return self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Here’s what you can do as a Guest User')]")))
#
#     @property
#     def first_screenshot(self):
#         return self.wait.until(ec.element_to_be_clickable((By.XPATH, "(//img[@style='cursor: pointer'])[1]")))
#
#     @property
#     def close_image(self):
#         return self.wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='inside close-image']")))
#
#     @property
#     def image_on_screen(self):
#         return self.wait.until(ec.visibility_of_all_elements_located((By.XPATH,"//img[@id = 'current-image']")))
#
#     def open_screenshot(self):
#         self.first_title.click()
#         self.first_screenshot.click()
#
#     def close_screenshot(self):
#         self.close_image.click()
