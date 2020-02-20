# from homework.hw10.contractors_county import ContractorPage
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
# from homework.hw10.base_page_county import BasePage
#
#
# class LandingPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     # @property
#     # def header(self):
#     #     return self.driver.find_elements_by_xpath("//*[contains(text(),'connect Construction')]")
#
#     @property
#     def contractor(self):
#         return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='CONTRACTORS']")))
#
#     def open(self):
#         self.driver.get("https://testkwidos.tk/")
#
#     # def check(self):
#     #     return len(self.header) == 1
#
#     def open_contractor(self):
#         self.contractor.click()
#         return ContractorPage(self.driver)
