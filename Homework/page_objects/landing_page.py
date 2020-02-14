from Homework.page_objects.offers_page import OffersPage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def offers(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH,"//*[text()='OFFERS']")))

    def open(self):
        self.driver.get("https://testkwidos.tk/")

    def open_offers(self):
        self.offers.click()
        return OffersPage(self.driver)
