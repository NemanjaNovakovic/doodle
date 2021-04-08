from selenium.webdriver.common.keys import Keys
from locators.locators import DashboardLocators

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    def create_new(self):
        self.driver.find_element(*DashboardLocators.create).click()

