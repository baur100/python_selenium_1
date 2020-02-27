from hwselenium13.pageobjects.base_page import BasePage
from hwselenium13.pageobjects.register_consumer_page import RegisterConsumerPage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from hwselenium13.pageobjects.blog_page import BlogPage
from hwselenium13.pageobjects.how_it_works import HowItWorksPage
from selenium.webdriver.common.action_chains import ActionChains



class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def header(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'connect Construction')]")

    @property
    def register_consumer(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH,"//*[text()='SERVICE CONSUMER']")))

    @property
    def blog(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='BLOG']")))

    @property
    def howItWorks(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='HOW IT WORKS']")))

    def open(self):
        self.driver.get("https://testkwidos.tk/")

    def check(self):
        return len(self.header)==1

    def open_register_consumer(self):
        self.register_consumer.click()
        return RegisterConsumerPage(self.driver)

    def open_blog(self):
        self.blog.click()
        return BlogPage(self.driver)

    def open_how_it_works(self):
        self.howItWorks.click()
        return HowItWorksPage(self.driver)

    # def mouse_hover(self):
    #     hov = ActionChains(self.driver).move_to_element(self.blog)
    #     hov.perform()
    #
    # def check_the_color(self):
    #     return self.blog.value_of_css_property("color")

    def is_hovered(self):
        color_before = self.blog.value_of_css_property("color")

        ActionChains(self.driver).move_to_element(self.blog).perform()

        color_after = self.blog.value_of_css_property("color")
        print(f"color before = {color_before} and color after = {color_after}")
        return color_before != color_after#doesn't work

