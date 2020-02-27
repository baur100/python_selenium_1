from hwselenium13.pageobjects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BlogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def blog(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@class='timeline-inverted']")))

    def count_blog(self):
        locator="//*[contains(text(),'Free For Homeowners')]"
        target =self.blog
        self.driver.execute_script('arguments[0].scrollIntoView();', target)
        count=1
        while 'KWIDOS IS THE PLACE' not in target.text:
            target= self.driver.execute_script("""
                return arguments[0].nextElementSibling
                """, target)
            self.driver.execute_script('arguments[0].scrollIntoView();', target)
            count+=1
        return count


