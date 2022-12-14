import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture()
def initiate_driver():
    driver.get("https://wellbecloud.aaneelcare.com/#!/login")
    driver.maximize_window()
    # time.sleep(20)

    yield driver

    driver.quit()
