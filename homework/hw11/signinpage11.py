from homework.hw11.base_page11 import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


class SigninPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def email_field(self):
        return self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#email")))

    def enter_email(self):
        return self.driver.find_element_by_css_selector("#email").send_keys("vladimir2133@gmail.com")

    @property
    def password_field(self):
        return self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#password")))

    def enter_password(self):
        return self.driver.find_element_by_css_selector("#password").send_keys("VVVlkjjgfd234!")

    @property
    def click_button(self):
        return self.driver.find_element_by_xpath("//button[@type='submit']")

    def all_sign_in(self):
        self.email_field.click()
        self.enter_email()
        self.password_field.click()
        self.enter_password()
        time.sleep(2)
        self.click_button.click()
