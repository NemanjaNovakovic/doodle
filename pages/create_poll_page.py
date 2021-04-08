from selenium.webdriver.common.keys import Keys
from locators.locators import CreatePollLocators

class CreatePollPage:

    def __init__(self, driver):
        self.driver = driver

    def create_new(self, polltitle, option1, option2):
        self.driver.find_element(*CreatePollLocators.title).click()
        self.driver.find_element(*CreatePollLocators.titletext).send_keys(polltitle, Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)
        self.driver.find_element(*CreatePollLocators.textoption).click()
        self.driver.find_element(*CreatePollLocators.option1).click()
        self.driver.find_element(*CreatePollLocators.option1).send_keys(option1, Keys.TAB, option2)
        self.driver.find_element(*CreatePollLocators.continue_button).click()
        self.driver.find_element(*CreatePollLocators.finish_button).click()
        #self.driver.find_element(*CreatePollLocators.email_addresses).send_keys(email)
        self.driver.find_element(*CreatePollLocators.send_button).click()







