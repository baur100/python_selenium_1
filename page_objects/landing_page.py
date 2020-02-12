from page_objects.contactor_page import ContractorPage


class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def header(self):
        return self.driver.find_elements_by_xpath("//*[contains(text(),'connect Construction')]")

    @property
    def contractor(self):
        return self.driver.find_element_by_xpath("//*[text()='CONTRACTORS']")

    def open(self):
        self.driver.get("https://testkwidos.tk/")

    def check(self):
        return len(self.header) == 1

    def open_contractor(self):
        self.contractor.click()
        return ContractorPage(self.driver)
