from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class ContractorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def dropdown_service_type(self):
        return self.driver.find_element_by_css_selector(".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")
        # return self.wait.until(ec.visibility_of_element_located(
        #     (By.CSS_SELECTOR, ".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")))

    def service(self,service):
        return self.driver.find_element_by_xpath(f"//*[text()='{service}']/preceding-sibling::div")

    def get_contractor(self,contractor_name):
        return self.driver.find_elements_by_xpath(f"//*[text()='{contractor_name}']")

    @property
    def close_dropdown(self):
        return self.driver.find_element_by_css_selector(".ui-multiselect-close.ui-corner-all")

    @property
    def state_dropdown(self):
        return self.driver.find_element_by_css_selector(".ui-dropdown-trigger-icon.ui-clickable.pi.pi-caret-down")

    @property
    def n_found(self):
        # return self.wait.until(ec.visibility_of_any_elements_located((By.CSS_SELECTOR,"h1")))
        return self.driver.find_elements_by_css_selector("h1")

    def state(self,state):
        return self.driver.find_element_by_xpath(f"//span[text()='{state}']")

    def click_dropdown(self):
        dropdown_service_type = self.driver.find_element_by_css_selector(".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")
        dropdown_service_type.click()

    def choose_contractor(self, service,state,county=""):
        self.dropdown_service_type.click()
        self.service(service).click()
        self.close_dropdown.click()
        self.state_dropdown.click()
        self.state(state).click()

    def is_not_found_message(self):
        return len(self.n_found) == 1

    def contractor_is_exist(self,name):
        return len(self.get_contractor(name))>=1





