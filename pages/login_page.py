from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import config

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")

    def login(self, username, password):
        """Logs in to the application with provided username and password."""
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
