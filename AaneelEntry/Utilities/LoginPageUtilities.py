from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AaneelEntry.Config.configdata import *
from AaneelEntry.Locators.HomePageLocators import *
from AaneelEntry.Locators.LoginPageLocators import *
from AaneelEntry.conftest import driver
from Explorra.Locators.LoginPageLocators import *


class LoginPageFunctions:

    def perform_login(self, username, password):
        self.fill_username(username)
        driver.find_element(by=By.CSS_SELECTOR, value=username_field).click()
        self.fill_password(password)
        driver.find_element(by=By.CSS_SELECTOR, value=password_field).click()

    def fill_username(self, username):
        WebDriverWait(driver, explicit_wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, username_field)))
        driver.find_element(by=By.CSS_SELECTOR, value=email_field).send_keys(username)

    def fill_password(self, password):
        WebDriverWait(driver, explicit_wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, password_field)))
        driver.find_element(by=By.CSS_SELECTOR, value=username_field).send_keys(password)
    def get_text(self, text_value):
        WebDriverWait(driver, explicit_wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, text_value)))
        # driver.find_element(by=By.CSS_SELECTOR, value=username_field).send_keys(password)

