from selenium.webdriver.support.ui import WebDriverWait

# https://selenium-python.readthedocs.io/waits.html
# this class | page is all about waits (explicit waits = wait until condition)
# self :
# self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.
# "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts.
# This method called when an object is created from the class and it allow the class to initialize the attributes of a class.

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)

