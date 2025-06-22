import pytest
from pages.login_page import LoginPage
from utils import config
from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_login_successful(setup):
    login_page = LoginPage(setup)
    login_page.login(config.USERNAME_TRUE, config.PASSWORD_TRUE)

    # Verify URL
    assert "logged-in-successfully" in setup.current_url

    # Verify text on page
    body_text = setup.find_element(By.TAG_NAME, "body").text
    assert "Congratulations" in body_text or "successfully logged in" in body_text

    # Verify Log out button displayed
    logout_button = setup.find_element(By.XPATH, "//a[text()='Log out']")
    assert logout_button.is_displayed()


@pytest.mark.negative
def test_login_invalid_username(setup):
    login_page = LoginPage(setup)
    login_page.login(config.USERNAME_FALSE, config.PASSWORD_TRUE)

    # Verify error message displayed
    error_msg = setup.find_element(By.ID, "error")
    assert error_msg.is_displayed()

    # Verify error message text
    assert "Your username is invalid!" in error_msg.text


@pytest.mark.negative
def test_login_invalid_password(setup):
    login_page = LoginPage(setup)
    login_page.login(config.USERNAME_TRUE, config.PASSWORD_FALSE)

    # Verify error message displayed
    error_msg = setup.find_element(By.ID, "error")
    assert error_msg.is_displayed()

    # Verify error message text
    assert "Your password is invalid!" in error_msg.text
