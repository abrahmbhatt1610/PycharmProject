import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture()
def initiate_driver():
    driver.get("https://login.advancedmd.com/")
    # driver.get("https://pm-wfe-102.advancedmd.com/amds/pm/app/index.html#/")
    driver.maximize_window()
    time.sleep(10)

    yield driver

    driver.quit()


