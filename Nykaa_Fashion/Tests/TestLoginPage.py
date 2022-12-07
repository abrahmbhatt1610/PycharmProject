import time

import pytest
from selenium.webdriver.common.by import By
from Nykaa_Fashion.Locators.LoginPageLocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Nykaa_Fashion.Config.configdata import *
from Nykaa_Fashion.Utlities.LoginPageUtilities import LoginPageFunctions
from Nykaa_Fashion.conftest import *


@pytest.mark.usefixture("initiate_driver")
class TestLoginPage:

    def test_verify_LoginPage(self, initiate_driver):
        driver = initiate_driver
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, account_button)))
        driver.find_element(by=By.CSS_SELECTOR, value=account_button).click()
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, login_button)))
        driver.find_element(by=By.CSS_SELECTOR, value=login_button).click()
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, cont_number)))
        driver.find_element(by=By.CSS_SELECTOR, value=cont_number).send_keys(mobile_number)
        driver.find_element(by=By.CSS_SELECTOR, value=submit_button).click()
        time.sleep(20)
        driver.find_element(by=By.CSS_SELECTOR, value=verify_otp).click()
        time.sleep(3)
        wrong_otp = driver.find_element(by=By.CSS_SELECTOR, value=wrong_otp_number).text
        assert wrong_otp == wrong_otp_number, "Your otp is wrong"
