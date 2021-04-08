from selenium.webdriver.common.by import By

class LandingLocators:
    login_button = (By.XPATH, "//*[text()='Log in']")


class LogInLocators:
    email = (By.NAME, "email")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//*[text()='Log in']")

class DashboardLocators:
    create = (By.XPATH, "//*[text()='Create']")

class CreateLocators:
    poll = (By.XPATH, "//*[text()='Group Poll']")

class CreatePollLocators:
    title = (By.XPATH, "//*[@class='d-pollTitleInputBar']")
    titletext = (By.XPATH, "//*[@placeholder='Enter title']")
    textoption = (By.LINK_TEXT, "Text")
    option1 = (By.XPATH, "//*[@placeholder='Option']")
    option2 = (By.XPATH, "//*[@placeholder='Add option']")
    continue_button = (By.XPATH, "//*[@id='d-wizardOptionsNavigationView']/div/div/div[2]/button[2]")
    finish_button = (By.XPATH, "//*[@id='d-wizardSettingsNavigationView']/div/div/div[2]/button[2]")
    email_addresses = (By.XPATH, "//*[@id='d-sharingView']/div/section[2]/div[1]/div/div[1]/input")
    send_button = (By.XPATH, "//*[@id='d-pollActionBarView']/div/div/div[3]/button")
    voting_success = (By.XPATH, "//*[text()='You have successfully voted']")



