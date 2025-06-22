import pytest
from pages.exceptions_page import ExceptionsPage
from utils import config
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    InvalidElementStateException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def exception_page(setup):
    page = ExceptionsPage(setup)
    page.open(config.EXCEPTION_URL)
    return page


def test_nosuch_element_exception(exception_page):
    exception_page.click_add_button()
    try:
        assert exception_page.get_row2_input().is_displayed()
    except NoSuchElementException:
        pytest.fail("Row 2 input field not found.")


def test_element_not_interactable_exception(exception_page):
    exception_page.click_add_button()
    exception_page.type_row2_input("Burger")
    try:
        exception_page.driver.find_element(By.NAME, "Save").click()
    except ElementNotInteractableException:
        exception_page.click_visible_save_button()
    assert "Burger" in exception_page.driver.page_source


def test_invalid_element_state_exception(exception_page):
    try:
        exception_page.get_row1_input().clear()
    except InvalidElementStateException:
        exception_page.click_edit_button()
        exception_page.get_row1_input().clear()
        exception_page.get_row1_input().send_keys("Sushi")
    assert "Sushi" in exception_page.get_row1_input().get_attribute("value")


def test_stale_element_reference_exception(exception_page):
    instructions = exception_page.get_instruction_element()
    exception_page.click_add_button()
    try:
        assert not instructions.is_displayed()
    except StaleElementReferenceException:
        assert True


def test_timeout_exception(exception_page):
    exception_page.click_add_button()
    with pytest.raises(TimeoutException):
        WebDriverWait(exception_page.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='row2']//input"))
        )
