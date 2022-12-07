import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import conftest as ct
import LoginPageLocator as lpl
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as ac, ActionChains


def login(self, initiate_driver):
    driver = initiate_driver
    driver.maximize_window()
    driver.find_element(by=By.CSS_SELECTOR, value=lpl.location_box).send_keys("Ahmedabad")
    # driver.find_element(by=By.CSS_SELECTOR, value=lpl.find_food_button).click()



