from hwselenium11.pageobjects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class OffersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @property
    def service_type_dropdown(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@class='ui-multiselect-label ui-corner-all']")))

    def service_type(self, service):
        return self.driver.find_element_by_xpath(f"//*[text()='{service}']")

    @property
    def service_type_dropdown_exit(self):
        return self.driver.find_element_by_css_selector(".pi.pi-times")

    @property
    def state_dropdown(self):
        return self.driver.find_element_by_xpath("//*[contains(@class,'ng-tns-c22-1 prime-')]")

    @property
    def county_dropdown(self):
        return self.driver.find_element_by_xpath("//*[@title='Select']")

    @property
    def all_county_checkbox(self):
        return self.driver.find_element_by_xpath("//*[contains(@class,'ui-widget-header ui-corner-all')]/*[1]/*[2]")

    def state(self, state):
        return self.driver.find_element_by_xpath(f"//span[text()='{state}']")

    @property
    def county_exit(self):
        return self.driver.find_element_by_xpath("//*[@class='pi pi-times']")

    @property
    def card_title(self):
        return self.driver.find_element_by_css_selector(".card-title.red-shape")

    @property
    def card_color(self):
        return self.driver.find_element_by_css_selector(".card-shape__green").value_of_css_property("background")

    @property
    def card_code(self):
        return self.driver.find_element_by_xpath("//*[@class='job-site-code job-site-code__color--green']")

    def click_service_type(self):
        self.service_type_dropdown.click()

    def choose_service_type(self, service_type):
        self.click_service_type()
        self.service_type(service_type).click()
        self.service_type_dropdown_exit.click()

    def choose_state(self, state):
        self.state_dropdown.click()
        self.state(state).click()

    def choose_all_county(self):
        self.county_dropdown.click()
        self.all_county_checkbox.click()
        self.county_exit.click()

    def check_card_by_title_color(self, title, color, code):
        return self.card_title.text==title and color in self.card_color and self.card_code.text==code





