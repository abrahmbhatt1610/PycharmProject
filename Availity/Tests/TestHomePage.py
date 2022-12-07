import time
import pytest
from selenium.webdriver.common.by import By
from Availity.Locators.HomePageLocators import *
from Availity.Locators.LoginPageLocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Availity.Config.configdata import *


@pytest.mark.usefixture("initiate_driver")
class TestHomePage:

    def test_verify_HomePage(self, initiate_driver):
        driver = initiate_driver
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, username_field)))
