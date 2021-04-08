import pytest
from pages.landing_page import LandingPage
from pages.login_page import LogInPage
from pages.dashboard_page import DashboardPage
from pages.create_page import CreatePage
from pages.create_poll_page import CreatePollPage
from locators.locators import CreatePollLocators

import time


@pytest.mark.usefixtures("setup")
class Test:
    def test_open_doodle(self):
        landing_page = LandingPage(self.driver)
        landing_page.open_page()
        landing_page.open_login()
        login_page = LogInPage(self.driver)
        login_page.set_user_inputs("doodle.test2021@gmail.com", "DoodleTest2021!")
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.create_new()
        create_page = CreatePage(self.driver)
        create_page.create_new()
        create_poll_page = CreatePollPage(self.driver)
        create_poll_page.create_new("Test Poll", "Option1", "Option2")
        time.sleep(10)
        assert CreatePollLocators.voting_success
