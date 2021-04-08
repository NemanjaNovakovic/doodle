from selenium.webdriver.common.keys import Keys
from locators.locators import LandingLocators

class LandingPage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("http://www.doodle.com")

    def open_login(self):
        self.driver.find_element(*LandingLocators.login_button).click()

