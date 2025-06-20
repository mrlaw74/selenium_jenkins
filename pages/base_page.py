from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(driver, self.timeout)

    def find(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        self.find(by_locator).click()

    def send_keys(self, by_locator, value):
        self.find(by_locator).send_keys(value)

    def get_text(self, by_locator):
        return self.find(by_locator).text

    def is_visible(self, by_locator):
        try:
            self.find(by_locator)
            return True
        except:
            return False
