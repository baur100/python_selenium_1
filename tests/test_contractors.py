from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class Test_Contractors:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/Users/tarapodolskiy/PycharmProjects/drivers/chromedriver")
        driver.implicitly_wait(3)
        driver.get("https://testkwidos.tk/")
        yield
        time.sleep(5)
        driver.quit()

    def test_offers(self, test_setup):
        offers = driver.find_element_by_xpath("//*[contains(text(), 'OFFERS')]")
        offers.click()

        service_type = driver.find_element_by_css_selector(".ui-multiselect-trigger-icon.ui-clickable.pi.pi-caret-down")
        service_type.click()

        select = driver.find_element_by_xpath("//label[contains(text(),'Air conditioning')]")
        select.click()

        close = driver.find_element_by_css_selector(".pi.pi-times")
        close.click()

        state_field = driver.find_element_by_css_selector(".ui-dropdown-trigger-icon.ui-clickable.pi.pi-caret-down")
        state_field.click()

        california = driver.find_element_by_xpath("//span[contains(text(),'California')]")
        california.click()

        text = driver.find_element_by_xpath("//*[contains(text(), 'house')]").text
        assert "house" in text



