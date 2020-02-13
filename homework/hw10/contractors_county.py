from homework.hw10.base_page_county import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class ContractorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def dropdown_service_type(self):
        return self.wait.until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, ".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")))

    def service1(self, service1):
        return self.driver.find_element_by_xpath(f"//*[text()='{service1}']/preceding-sibling::div")

    def service2(self, service2):
        return self.driver.find_element_by_xpath(f"//*[text()='{service2}']/preceding-sibling::div")

    @property
    def close_dropdown(self):
        return self.driver.find_element_by_css_selector(".ui-multiselect-close.ui-corner-all")

    @property
    def state_dropdown(self):
        return self.driver.find_element_by_css_selector(".ui-dropdown-trigger-icon.ui-clickable.pi.pi-caret-down")

    @property
    def n_found(self):
        return self.wait.until(ec.visibility_of_any_elements_located((By.CSS_SELECTOR, "h1")))

    def state(self, state):
        return self.driver.find_element_by_xpath(f"//span[text()='{state}']")

    def click_dropdown(self):
        dropdown_service_type = self.driver.find_element_by_css_selector(
            ".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")
        dropdown_service_type.click()

    @property
    def dropdown_service_county(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                 '//*[@id="main-panel"]/div/div/div/app-contractor'
                                                                 '-cmp/div/div/div/div[1]/div/div[2]/div['
                                                                 '4]/p-multiselect/div/div[3]/span')))

    def county(self, county):
        return self.driver.find_element_by_xpath(f"//*[text()='{county}']")

    def county_dropdown_click(self):
        dropdown_service_county = self.driver.find_element_by_xpath((
            "//*[@id='main-panel']/div/div/div/app-contractor-cmp/div/div/div/div[1]/div/div[2]/div["
            "4]/p-multiselect/div/div[3]/span)"))
        dropdown_service_county.click()

    @property
    def close_dropdown_county(self):
        return self.driver.find_element_by_xpath('//*[@id="main-panel"]/div/div/div/app-contractor-cmp/div/div/div'
                                                 '/div[1]/div/div[2]/div[4]/p-multiselect/div/div[4]/div[1]/a/span')

    def choose_contractor(self, service1, service2, state, county):
        self.dropdown_service_type.click()
        self.service1(service1).click()
        self.service2(service2).click()
        self.close_dropdown.click()
        self.state_dropdown.click()
        self.state(state).click()
        self.dropdown_service_county.click()
        self.county(county).click()
        self.close_dropdown_county.click()

    def is_not_found_message(self):
        return len(self.n_found) == 1
