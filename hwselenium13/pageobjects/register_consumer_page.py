from hwselenium13.pageobjects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class RegisterConsumerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def reg_title(self):
        return self.driver.find_elements_by_xpath("//*[@class='card-header']")

    @property
    def first_name_textbox(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH,"//*[@formcontrolname='firstName']")))

    @property
    def last_name_textbox(self):
        return self.driver.find_element_by_xpath("//*[@formcontrolname='lastName']")

    @property
    def phone_textbox(self):
        return self.driver.find_element_by_xpath("//*[@formcontrolname='phone']")

    @property
    def email_textbox(self):
        return self.driver.find_element_by_xpath("//*[@formcontrolname='email']")

    @property
    def password_textbox(self):
        return self.driver.find_element_by_xpath("//*[@formcontrolname='password']")

    @property
    def terms_check_box(self):
        return self.driver.find_element_by_xpath("//*[@class='col-lg-12 col-xs-12 col-md-12 checkbox-block']/p-checkbox")

    @property
    def button(self):
        return self.driver.find_element_by_xpath("//*[@type='submit']")

    @property
    def alreadyExist(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='alert alert-danger']")))


    def check_in(self):
        return len(self.reg_title)==1

    def fill_out_form(self, first, last, phone, email, passw):
        self.first_name_textbox.send_keys(first)
        self.last_name_textbox.send_keys(last)
        self.phone_textbox.send_keys(phone)
        self.email_textbox.send_keys(email)
        self.password_textbox.send_keys(passw)
        self.terms_check_box.click()

    def click_button(self):
        self.button.click()

    def accountExists(self, str):
        return self.alreadyExist.text == str










