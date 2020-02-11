import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions, wait


class TestOffers:
    @pytest.fixture()
    def test_setup(self):
        global driver
        global wait
        driver = webdriver.Chrome(executable_path="./chromedriver")
        wait = WebDriverWait(driver, 5)
        # driver.implicitly_wait(5)
        driver.get("https://kwidos.com/")
        yield
        time.sleep(3)
        driver.quit()

    def test_offers(self, test_setup):
        offers = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='OFFERS']")))
        offers.click()

        dropdown_service_type = wait.until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, ".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")))
        driver.find_element_by_css_selector(".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")
        dropdown_service_type.click()

        search = wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//*[@class='ui-inputtext ui-widget ui-state-default ui-corner-all']")))
        search.click()
        search.send_keys("electric")

        electric_checkbox = driver.find_element_by_xpath(
            "//*[@id='main-panel']/div/div/div/app-offer-search/div/div/div/div[1]/div/div[2]/div["
            "2]/p-multiselect/div/div[4]/div[2]/ul/li[23]/label ")
        electric_checkbox.click()

        dropdown_service_type = wait.until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, ".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")))
        driver.find_element_by_css_selector(".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")
        dropdown_service_type.click()

        state_dropdown = driver.find_element_by_css_selector(".ui-dropdown-trigger-icon.ui-clickable.pi.pi-caret-down")
        state_dropdown.click()

        search2 = wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//*[@class='ui-dropdown-filter ui-inputtext ui-widget ui-state-default ui-corner-all']")))
        search2.click()
        search2.send_keys("florida")

        florida_checkbox = driver.find_element_by_xpath("//*[@id='main-panel']/div/div/div/app-offer-search/div/div"
                                                        "/div/div[1]/div/div[2]/div[3]/p-dropdown/div/div[4]/div["
                                                        "2]/ul/li")
        florida_checkbox.click()

        breaker_box_text = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[contains(text(),"
                                                                                                "'Breaker box')]")))
        assert breaker_box_text.text == "Breaker box"

        color = driver.find_element_by_xpath("//*[@class='card card-shape__green']")
        background_color = color.value_of_css_property("background-color")

        assert background_color == "rgba(224, 241, 222, 1)"


