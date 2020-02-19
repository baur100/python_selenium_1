from Homework.page_objects.offers_page import OffersPage
from Homework.page_objects.sign_in_page import SignInPage
from Homework.page_objects.blog_page import BlogPage
from Homework.page_objects.how_it_works_page import HowItWorksPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import time

class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def offers(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH,"//*[text()='OFFERS']")))

    @property
    def sign_in(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH,"//*[text()='SIGN IN']")))

    @property
    def blog(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='BLOG']")))

    @property
    def how_it_works(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='HOW IT WORKS']")))

    def open(self):
        self.driver.get("https://testkwidos.tk/")

    def open_offers(self):
        self.offers.click()
        return OffersPage(self.driver)

    def open_sign_in(self):
        self.sign_in.click()
        return SignInPage(self.driver)

    def open_blog(self):
        self.blog.click()
        return BlogPage(self.driver)

    def open_how_it_works(self):
        self.how_it_works.click()
        return HowItWorksPage(self.driver)

    @property
    def menu_items_list(self):
        return self.wait.until(ec.visibility_of_all_elements_located((By.XPATH,"//a//p")))

    def hover(self):
        for item in self.menu_items_list:
            print('\nItem:', item.text,'\nColor before',item.value_of_css_property('color'))
            ActionChains(self.driver).move_to_element(item).perform()
            print('Color after', item.value_of_css_property('color'))





