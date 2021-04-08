from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            return webdriver.Chrome(ChromeDriverManager().install(), options=options)
