from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class ContractorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def dropdown_service_type(self):
        return self.wait.until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, ".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")))

    @property
    def close_dropdown(self):
        return self.driver.find_element_by_css_selector(".ui-multiselect-close.ui-corner-all")

    @property
    def state_dropdown(self):
        return self.driver.find_element_by_css_selector(".ui-dropdown-trigger-icon.ui-clickable.pi.pi-caret-down")

    @property
    def title(self):
        return self.wait.until(ec.visibility_of_any_elements_located((By.CSS_SELECTOR,"h1")))

    def service(self, service):
        return self.driver.find_element_by_xpath(f"//*[text()='{service}']/preceding-sibling::div")

    def state(self,state):
        return self.driver.find_element_by_xpath(f"//span[text()='{state}']")

    def click_dropdown(self):
        dropdown_service_type = self.driver.find_element_by_css_selector(".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")
        dropdown_service_type.click()

    def choose_contractor(self, service,state,county=""):
        self.dropdown_service_type.click()
        self.service(service).click()
        self.dropdown_service_close.click()
        self.state_dropdown.click()
        self.state(state).click()

    def is_title_exist(self):
        return len(self.title) == 1

    def is_status_exist(self):
        return len(self.status) == 1

    def is_originated_by_exist(self):
        return len(self.title) == 1

    def is_r_letter_exist(self):
        return len(self.title) == 1





