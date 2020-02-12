class ContractorPage:
    def __init__(self,driver):
        self.driver = driver


    @property
    def dropdown_service_type(self):
        return self.driver.find_element_by_css_selector(".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")

    def service(self,service):
        return self.driver.find_element_by_xpath(f"//*[text()='{service}']/preceding-sibling::div")

    @property
    def close_dropdown(self):
        return self.driver.find_element_by_css_selector(".ui-multiselect-close.ui-corner-all")

    @property
    def state_dropdown(self):
        return self.driver.find_element_by_css_selector(".ui-dropdown-trigger-icon.ui-clickable.pi.pi-caret-down")

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


