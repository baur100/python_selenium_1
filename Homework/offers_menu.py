import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestOffersMenu:

    @pytest.fixture()
    def setup(self):
        global driver
        global wait
        driver = webdriver.Chrome(executable_path="./chromedriver")
        wait = WebDriverWait(driver,5)
        driver.get("https://testkwidos.tk/")
        yield
        time.sleep(5)
        driver.quit()

    @pytest.mark.usefixtures("setup")
    def test_offers(self):
        offers = wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='OFFERS']")))
        offers.click()

        first_caret = wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(@class, 'caret')][position() = 1]")))
        first_caret.click()

        air_check = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Air conditioning']/preceding-sibling::div")))
        air_check.click()

        exit = driver.find_element_by_xpath("//span[@class='pi pi-times']")
        exit.click()

        second_caret = driver.find_element_by_xpath("//span[@class = 'ui-dropdown-trigger-icon ui-clickable pi pi-caret-down']")
        second_caret.click()

        state = driver.find_element_by_xpath('//li/span[text() =  "California"]')
        state.click()

        house_text = wait.until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'house')]")))
        assert house_text.text == "house", "Text should be 'house'"

        air_text = wait.until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'Air conditioning')]")))
        assert air_text.text == "Air conditioning", "Text should be 'Air conditioning'"

        card = driver.find_element_by_xpath("//div[@class='card card-shape__green']")
        background = card.value_of_css_property("background-color")

        assert background == "rgba(224, 241, 222, 1)", "Color should be 'rgba(224, 241, 222, 1)'"



    @pytest.mark.usefixtures("setup")
    def test_drop_select(self):
        offers = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='OFFERS']")))
        offers.click()

        second_caret = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class = 'ui-dropdown-trigger-icon ui-clickable pi pi-caret-down']")))
        second_caret.click()

        states = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='ui-dropdown-items-wrapper']/ul/li/span")))

        for state in states:
            if state.text == 'Wyoming':
                state.click()
                selected_option = state.text
                break

        assert selected_option == 'Wyoming', "Selected option should be Wyoming"



    @pytest.mark.usefixtures("setup")
    def test_blog_scroll_down(self):
        blog = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='BLOG']")))
        blog.click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        bottom_text = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Kwidos is the place for new businesses']")))

        assert bottom_text.text == 'KWIDOS IS THE PLACE FOR NEW BUSINESSES', 'Text should be "KWIDOS IS THE PLACE FOR NEW BUSINESSES"'







