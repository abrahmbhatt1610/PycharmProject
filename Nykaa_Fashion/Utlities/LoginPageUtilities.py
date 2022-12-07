from selenium.webdriver.common.by import By

from Nykaa_Fashion.conftest import driver
from Nykaa_Fashion.Locators.LoginPageLocators import *


class LoginPageFunctions:

    def perform_login(self, mobile_number, otp):
        self.fill_username(mobile_number)
        driver.find_element(by=By.CSS_SELECTOR, value=cont_number).click()
        self.fill_password(otp)
        driver.find_element(by=By.CSS_SELECTOR, value=verify_otp).click()

    def fill_username(self, mobile_number):
        pass
