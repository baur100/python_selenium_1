# class SignInPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     @property
#     def email(self):
#         return self.wait.until(ec.presence_of_element_located((By.ID, "email")))
#
#     @property
#     def password(self):
#         return self.driver.find_element_by_id("password")
#
#     @property
#     def submit_button(self):
#         return self.driver.find_element_by_xpath("//button[@type='submit']")
#
#     @property
#     def show_psswd(self):
#         return self.driver.find_element_by_xpath("//i[@class='fa fa-eye']")
#
#     def get_consumer(self):
#         return self.wait.until(ec.presence_of_element_located((By.XPATH, "//span[@class='user-name-individual']")))
#
#     def login(self, email, password, first_name, last_name):
#         self.email.send_keys(email)
#         self.password.send_keys(password)
#         self.show_psswd.click()
#         self.submit_button.click()
#         # consumer_name = self.get_consumer().text
#         # consumer_name.strip()
#         # print(consumer_name)
#         #
#         # assert consumer_name == f"{first_name} {last_name}"
