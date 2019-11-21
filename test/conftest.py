import pytest
from selenium import webdriver

@pytest.yield_fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()