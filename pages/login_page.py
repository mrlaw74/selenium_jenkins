from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import config

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")

    def login(self):
        self.send_keys(self.USERNAME, config.USERNAME)
        self.send_keys(self.PASSWORD, config.PASSWORD)
        self.click(self.LOGIN_BUTTON)
