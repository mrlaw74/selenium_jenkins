from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExceptionsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click_add_button(self):
        self.driver.find_element(By.ID, "add_btn").click()

    def click_edit_button(self):
        self.driver.find_element(By.ID, "edit_btn").click()

    def type_row2_input(self, text):
        input_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='row2']//input")))
        input_box.send_keys(text)

    def click_visible_save_button(self):
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@name='Save'])[2]")))
        save_button.click()

    def get_error_element(self):
        return self.driver.find_element(By.ID, "error")

    def get_instruction_element(self):
        return self.driver.find_element(By.ID, "instructions")

    def get_row2_input(self):
        return self.driver.find_element(By.XPATH, "//div[@id='row2']//input")

    def get_row1_input(self):
        return self.driver.find_element(By.ID, "row1_input")
