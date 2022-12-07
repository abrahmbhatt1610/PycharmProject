import time
from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import LoginPageLocator as lpl
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as ac, ActionChains


@pytest.mark.usefixture("initiate_driver", "maximize_windows", "navigate_to_login_page")
class TestLoginPage:
    @pytest.mark.usefixture("initiate_driver")
    def test_verify_login(self, initiate_driver):
        driver = initiate_driver
        driver.maximize_window()
        # element_text = driver.find_element(by=By.CSS_SELECTOR, value=lpl.city)
        locate = driver.find_element(by=By.CSS_SELECTOR, value=lpl.locate_me_button)
        locate.click()
        # time.sleep(100)

        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(lpl.enter_city))
        # driver.find_element(by=By.CSS_SELECTOR, value=lpl.enter_city).click()
        # driver.find_element(by=By.CSS_SELECTOR, value=lpl.sign_in_button).click()
        # driver.find_element(by=By.CSS_SELECTOR, value=lpl.Phone_number_login).send_keys("7984879566")

        # sign_button = driver.find_element(by=By.CSS_SELECTOR, value=lpl.sign_in_button)
        # sign_button.click()

        # phone_number = driver.find_element(by=By.CSS_SELECTOR, value=lpl.Phone_number_login).send_keys(7984879566)
        # WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(By.CSS_SELECTOR, lpl.otp_for_login))
        # driver.find_element(by=By.CSS_SELECTOR, value=lpl.verify_button).click()
