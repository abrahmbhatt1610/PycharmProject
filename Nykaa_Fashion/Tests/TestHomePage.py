import time
import pytest
from selenium.webdriver.common.by import By
from Nykaa_Fashion.Locators.HomePageLocators import *
from Nykaa_Fashion.Locators.LoginPageLocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Nykaa_Fashion.Config.configdata import *


@pytest.mark.usefixture("initiate_driver")
class TestHomePage:

    def test_verify_HomePage(self, initiate_driver):
        driver = initiate_driver
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, account_button)))
        driver.find_element(by=By.CSS_SELECTOR, value=account_button).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, login_button)))
        driver.find_element(by=By.CSS_SELECTOR, value=login_button).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, cont_number)))
        driver.find_element(by=By.CSS_SELECTOR, value=cont_number).send_keys(mobile_number)
        driver.find_element(by=By.CSS_SELECTOR, value=submit_button).click()
        time.sleep(20)
        driver.find_element(by=By.CSS_SELECTOR, value=verify_otp).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, all_brands)))
        driver.find_element(by=By.CSS_SELECTOR, value=all_brands).click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, adidas)))
        driver.find_element(by=By.CSS_SELECTOR, value=adidas).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, get_product)))
        driver.find_element(by=By.CSS_SELECTOR, value=get_product).click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, add_to_bag)))
        driver.find_element(by=By.XPATH, value=select_size).click()
        driver.find_element(by=By.CSS_SELECTOR, value=add_to_bag).click()
        time.sleep(3)
        driver.find_element(by=By.CSS_SELECTOR, value=view_bag).click()
        time.sleep(5)
        # driver.switch_to.window(driver.switch_to.active_element)
        driver.find_element(by=By.CSS_SELECTOR, value=move_to_wishlist).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, wishlist_button)))
        driver.find_element(by=By.CSS_SELECTOR, value=wishlist_button).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, proceed_to_buy)))
        driver.find_element(by=By.CSS_SELECTOR, value=proceed_to_buy).click()

