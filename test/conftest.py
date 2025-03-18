import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()