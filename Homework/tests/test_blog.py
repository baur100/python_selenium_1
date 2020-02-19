import pytest
from selenium import webdriver
from Homework.page_objects.landing_page import LandingPage


class TestBlog:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/Users/lanapaulikava/PycharmProjects/python_selenium_1/Homework/chromedriver")
        yield
        driver.quit()

    @pytest.mark.skip
    def test_count_blogs(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        blog_page = landing_page.open_blog()
        count = blog_page.blogs_count()
        assert count == 12, "Number of blogs should be 12!"
