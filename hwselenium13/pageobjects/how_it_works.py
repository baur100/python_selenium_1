from hwselenium13.pageobjects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class HowItWorksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def take_screenshot(self, name):
        screen_shot=self.driver.save_screenshot(name)


