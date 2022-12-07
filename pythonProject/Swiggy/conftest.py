import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def initiate_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.swiggy.com/")
    driver.maximize_window()
    # time.sleep(20)

    yield driver

    driver.quit()
