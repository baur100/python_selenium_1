from homework.hw11.base_page11 import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


class HowItWorksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def guest_user(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='accordion']/div/a/div/h4")))

    def click_guest_user(self):
        return self.guest_user.click()

    def click_screenshot(self):
        return self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='collapseOne']/div/div/div[1]/div/div[2]/div/img"))).click()

    def close_screenshot(self):
        return self.wait.until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@id='modal-gallery-container']/ks-upper-buttons/header/a/div"))).click()

    def all_how_it_works(self):
        self.click_guest_user()
        self.click_screenshot()
        time.sleep(3)
        self.close_screenshot()

