import pytest
from selenium.webdriver.common.by import By
from AaneelEntry.Locators.LoginPageLocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from AaneelEntry.Config.configdata import *


@pytest.mark.usefixture("initiate_driver")
class TestLoginPage:

    def test_verify_login(self, initiate_driver):
        driver = initiate_driver
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, username_field)))

        driver.find_element(by=By.CSS_SELECTOR, value=username_field).send_keys(username)
        driver.find_element(by=By.CSS_SELECTOR, value=password_field).send_keys(password)
        driver.find_element(by=By.CSS_SELECTOR, value=login_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, agree_button)))
        driver.find_element(by=By.CSS_SELECTOR, value=agree_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, alert_popup_close)))
        driver.find_element(by=By.CSS_SELECTOR, value=alert_popup_close).click()
        ActionChains.scroll_to_element(self, )