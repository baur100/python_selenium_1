from hwselenium11.pageobjects.offers_page import OffersPage
from hwselenium11.pageobjects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @property
    def header(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'connect Construction')]")

    @property
    def offers(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH,"//*[text()='OFFERS']")))

    def open(self):
        self.driver.get("https://testkwidos.tk/")

    def check(self):
        return len(self.header)==1

    def open_offers(self):
        self.offers.click()
        return OffersPage(self.driver)




