import time

import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def initiate_driver():
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.get("https://mytools.gatewayedi.com/LogOn?ReturnUrl=%2fdefault.aspx")
    driver.maximize_window()

    time.sleep(10)

    yield driver

    driver.quit()

