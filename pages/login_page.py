from selenium.webdriver.common.keys import Keys
from locators.locators import LogInLocators

class LogInPage:

    def __init__(self, driver):
        self.driver = driver

    def set_user_inputs(self, email, password):
        self.driver.find_element(*LogInLocators.email).click()
        self.driver.find_element(*LogInLocators.email).send_keys(email)
        self.driver.find_element(*LogInLocators.password).click()
        self.driver.find_element(*LogInLocators.password).send_keys(password, Keys.ENTER)
