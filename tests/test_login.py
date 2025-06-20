import pytest
from pages.login_page import LoginPage
from utils import config

@pytest.mark.smoke
def test_login_successful(setup):
    login_page = LoginPage(setup)
    login_page.login()
    assert "Logged In" in setup.title

@pytest.mark.smoke
def test_login_fail(setup):
    login_page = LoginPage(setup)
    login_page.login()
    assert "Logged In" not in setup.title