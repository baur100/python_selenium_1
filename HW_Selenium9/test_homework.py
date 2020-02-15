import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestOffers:
    @pytest.fixture()
    def test_setup(self):
        global driver
        global wait

        driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        wait = WebDriverWait(driver,5)
        driver.get("https://testkwidos.tk/")
        yield
        time.sleep(5)
        driver.quit()

    def test_offers(self,test_setup):
        offers = wait.until(conditions.element_to_be_clickable((By.XPATH,"//*[text()='OFFERS']")))
        offers.click()
        servise_type = wait.until(conditions.element_to_be_clickable((By.XPATH, "//*[@class='ui-multiselect-label ui-corner-all']")))
        servise_type.click()
        ac_checkbox=driver.find_element_by_xpath("//*[text()='Air conditioning']")
        ac_checkbox.click()
        dropdown_exit=driver.find_element_by_css_selector(".pi.pi-times")
        dropdown_exit.click()
        state_drop=driver.find_element_by_xpath("//*[contains(@class,'ng-tns-c22-1 prime-')]")
        state_drop.click()
        CA=driver.find_element_by_xpath("//span[text()='California']")
        CA.click()
        result=wait.until(conditions.visibility_of_element_located((By.CSS_SELECTOR, ".card-title.red-shape")))
        color=driver.find_element_by_css_selector(".card-shape__green").value_of_css_property("background")
        assert result.text=="house" and "rgb(224, 241, 222)" in color

    def test_state_WY(self, test_setup):
        offers = wait.until(conditions.element_to_be_clickable((By.XPATH, "//*[text()='OFFERS']")))
        offers.click()
        servise_type = wait.until(
        conditions.element_to_be_clickable((By.XPATH, "//*[@class='ui-multiselect-label ui-corner-all']")))
        servise_type.click()
        ac_checkbox = wait.until(conditions.element_to_be_clickable((By.XPATH,"//*[text()='Air conditioning']")))
        ac_checkbox.click()
        dropdown_exit = driver.find_element_by_css_selector(".pi.pi-times")
        dropdown_exit.click()
        state_drop = driver.find_element_by_xpath("//*[contains(@class,'ng-tns-c22-1 prime-')]")
        state_drop.click()
        target=driver.find_element_by_xpath("//span[text()='Wyoming']")
        driver.execute_script('arguments[0].scrollIntoView(true);', target)
        target.click()
        not_found_list = wait.until(conditions.visibility_of_any_elements_located((By.XPATH, "//*[text()='Offers not found']")))
        assert len(not_found_list) == 1

    def test_scroll_blog(self, test_setup):
        blog=wait.until(conditions.element_to_be_clickable((By.XPATH, "//*[text()='BLOG']")))
        blog.click()
        time.sleep(2)
        target = driver.find_element_by_xpath("//*[contains(text(),'Kwidos is the place')]")
        driver.execute_script('arguments[0].scrollIntoView();', target)
        assert 'KWIDOS IS THE PLACE' in target.text




