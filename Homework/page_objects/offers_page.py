# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__),”...”,”...”))
from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

class OffersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def dropdown_service_type(self):
        return self.wait.until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, ".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")))

    @property
    def dropdown_service_close(self):
        return self.driver.find_element_by_css_selector(".ui-multiselect-close.ui-corner-all")

    @property
    def dropdown_state(self):
        return self.driver.find_element_by_css_selector(".ui-dropdown-trigger-icon.ui-clickable.pi.pi-caret-down")

    @property
    def dropdown_county(self):
        return self.driver.find_element_by_xpath("(//*[@class='ui-multiselect-trigger-icon ui-clickable pi pi-caret-down'])[2]")

    @property
    def dropdown_county_close(self):
        return self.driver.find_element_by_css_selector(".pi.pi-times")

    @property
    def title(self):
        return self.wait.until(ec.visibility_of_any_elements_located((By.CSS_SELECTOR,"h3")))

    @property
    def status(self):
        return self.wait.until(ec.visibility_of_any_elements_located((By.XPATH, "//p[text()='Accepting bids']")))

    @property
    def service(self):
        return self.wait.until(ec.visibility_of_any_elements_located((By.XPATH, "//p[contains(text(),'Air conditioning')]")))

    @property
    def originated_by(self):
        return self.wait.until(ec.visibility_of_any_elements_located((By.CSS_SELECTOR, "//p[text()='Home Owner']")))

    @property
    def r_letter(self):
        return self.wait.until(ec.visibility_of_any_elements_located((By.XPATH, "//*[@class='job-site-code job-site-code__color--green'][text()='R']")))

    @property
    def all_counties(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH,"(//*[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default'])[1]")))

    def choose_service_type(self, service):
        self.dropdown_service_type.click()
        service_type = self.wait.until(ec.visibility_of_element_located((By.XPATH,f"//*[text()='{service}']/preceding-sibling::div")))
        service_type.click()
        self.dropdown_service_close.click()

    def choose_state(self,state):
        self.dropdown_state.click()
        state = self.driver.find_element_by_xpath(f"//span[text()='{state}']")
        state.click()

    def choose_all_counties(self):
        self.dropdown_county.click()
        time.sleep(2)
        self.all_counties.click()
        self.dropdown_county_close.click()

    def is_title_exist(self):
        return len(self.title) == 1

    def is_status_exist(self):
        return len(self.status) == 1

    def is_service_exist(self):
        return len(self.title) == 1

    def is_originated_by_exist(self):
        return len(self.title) == 1

    def is_r_letter_exist(self):
        return len(self.title) == 1



