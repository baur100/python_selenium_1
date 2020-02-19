from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BlogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def blogs_count(self):
        blogs = self.wait.until(ec.visibility_of_all_elements_located((By.XPATH, "//span[@class='label label-danger']")))
        for blog in blogs:
            print(blog.text)
        return len(blogs)






