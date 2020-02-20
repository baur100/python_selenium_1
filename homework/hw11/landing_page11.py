

from selenium.webdriver import ActionChains

from homework.hw11.how_it_works11 import HowItWorksPage
from homework.hw11.signinpage11 import SigninPage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from homework.hw11.base_page11 import BasePage
from homework.hw11.blog_number11 import BlogPage


class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def sign_in(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='SIGN IN']")))

    def open(self):
        self.driver.get("https://testkwidos.tk/")

    def open_sign_in(self):
        self.sign_in.click()
        return SigninPage(self.driver)

    @property
    def how_it_works(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//li[4]/a/p")))

    def open_how_it_works(self):
        self.how_it_works.click()
        return HowItWorksPage(self.driver)

    @property
    def blog(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='BLOG']")))

    def open_blog(self):
        self.blog.click()
        return BlogPage(self.driver)

    # this part is a copy of Lana's HW ( it's too hard)

    @property
    def menu(self):
        return self.wait.until(ec.visibility_of_all_elements_located((By.XPATH, "//a//p")))

    def hover(self):
        for item in self.menu:
            print('\nItem:', item.text, '\nColor before', item.value_of_css_property('color'))
            ActionChains(self.driver).move_to_element(item).perform()
            print('Color after', item.value_of_css_property('color'))
