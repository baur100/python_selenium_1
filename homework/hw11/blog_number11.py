from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from homework.hw11.base_page11 import BasePage


class BlogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def all_blogs(self):
        total = self.wait.until(
            ec.visibility_of_all_elements_located((By.XPATH, "//span[@class='label label-danger']")))
        i = len(total)
        if i == 12:
            return 12
        return False

