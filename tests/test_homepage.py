import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_homepage_title(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title

def test_homepage_header(driver):
    driver.get("https://example.com")
    header = driver.find_element(By.TAG_NAME, "h1")
    assert header.text == "Example Domain"