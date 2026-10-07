import pytest
from selenium import webdriver
#urls:
home_page_url = 'https://www.automationexercise.com/'


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(home_page_url)
    yield driver
    driver.quit()