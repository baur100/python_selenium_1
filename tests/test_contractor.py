import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.common.by import By

class TestContractor:
    @pytest.fixture()
    def test_setup(self):
        global driver
        global wait

        driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        wait = WebDriverWait(driver,5)
        # driver.implicitly_wait(5)
        driver.get("https://testkwidos.tk/")
        yield
        time.sleep(5)
        driver.quit()

    def test_contractor(self,test_setup):
        contractor = wait.until(conditions.element_to_be_clickable((By.XPATH,"//*[text()='CONTRACTORS']")))
        contractor.click()

        dropdown_service_type = wait.until(conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")))
        driver.find_element_by_css_selector(".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")
        dropdown_service_type.click()
        ac_checkbox=driver.find_element_by_xpath("//*[text()='Air conditioning']/preceding-sibling::div")
        ac_checkbox.click()
        close_dropdown = driver.find_element_by_css_selector(".ui-multiselect-close.ui-corner-all")
        close_dropdown.click()
        state_dropdown=driver.find_element_by_css_selector(".ui-dropdown-trigger-icon.ui-clickable.pi.pi-caret-down")
        state_dropdown.click()
        arizona = driver.find_element_by_xpath("//span[text()='Arizona']")
        arizona.click()

        not_found_list = wait.until(conditions.visibility_of_any_elements_located((By.XPATH,"//*[text()='Contractors not found']")))
        assert len(not_found_list) == 1



        # x= True
        # time_w = 0
        # while x or time_w <=5:
        #     try:
        #         driver.find_elements_by_xpath("Locator")
        #         x=False
        #     except NoSuchElementException:
        #         time.sleep(0.5)
        #         time_w+=0.5









