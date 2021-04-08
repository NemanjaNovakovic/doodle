from selenium.webdriver.common.keys import Keys
from locators.locators import CreateLocators

class CreatePage:

    def __init__(self, driver):
        self.driver = driver

    def create_new(self):
        self.driver.find_element(*CreateLocators.poll).click()

