import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

@pytest.fixture()
def initiate_driver():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.com")
    driver.maximize_window()
    yield driver
    driver.quit()





