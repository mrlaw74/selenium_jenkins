# conftest.py
import pytest
import os
import sys
import os
from selenium import webdriver
from utils import config

# Ensure root path is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Hook: Capture test result and attach to request.node
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to get the report
    outcome = yield
    rep = outcome.get_result()

    # Save result to item (used later in fixture)
    setattr(item, "rep_" + rep.when, rep)

# Fixture with screenshot-on-failure logic
@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config.URL)

    yield driver

    # Only capture screenshot if the test failed during the call phase
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_path = os.path.join("reports", f"failure_{request.node.name}.png")
        driver.save_screenshot(screenshot_path)
        print(f"[Screenshot saved] {screenshot_path}")

    driver.quit()
