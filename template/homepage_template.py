from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from tollroads.base_page_toalroads import BasePage
from tollroads.sign_in_tollroads import SigninPage
from selenium.webdriver import ActionChains


# this class is for homepage


class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

# get to click

    @property
    def covid_ad(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, '')))

# open homepage

    def open(self):
        self.driver.get("")

# function to close pop up

    def close_covid_ad(self):
        self.covid_ad.click()
        return SigninPage(self.driver)

# send keys

    def enter_email(self):
        return self.driver.find_element_by_xpath('').send_keys("")


# scroll down


    def scroll_down(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


#  dropdown menu

    @pytest.mark.usefixtures("setup")
    def test_drop_select(self):
        offers = wait.until(ec.presence_of_element_located((By.XPATH, "//*[text()='OFFERS']")))
        offers.click()



# count function

    def all_blogs(self):
        total = self.wait.until(
            ec.visibility_of_all_elements_located((By.XPATH, "")))
        i = len(total)
        if i == 10:
            return 10
        return False


# hover on with print colors before and after (from selenium.webdriver import ActionChains)

    @property
    def menu(self):
        return self.wait.until(ec.visibility_of_all_elements_located((By.XPATH, "")))

    def hover(self):
        for item in self.menu:
            print('\nItem:', item.text, '\nColor before', item.value_of_css_property('color'))
            ActionChains(self.driver).move_to_element(item).perform()
            print('Color after', item.value_of_css_property('color'))
