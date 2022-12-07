import time
import pandas as pd

import driver as driver
import pytest
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from AaneelEntry.Locators.HomePageLocators import *
from AaneelEntry.Locators.LoginPageLocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from AaneelEntry.Config.configdata import *
# from AaneelEntry.Locators.LoginPageLocators import username_field, password_field, login_button
from Explorra.Aaneel.aaneel_credentials import user_name


# @pytest.mark.usefixture("initiate_driver")
# class TestHomePage:

def HomePage_flow(driver=None):
    driver = driver.get_url('https://wellbecloud.aaneelcare.com/#!/Scheduling/MemberAppointment?isBillerReview=true')
    # WebDriverWait(driver, 30).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, username_field)))
    #
    # driver.find_element(by=By.CSS_SELECTOR, value=username_field).send_keys(username)
    # driver.find_element(by=By.CSS_SELECTOR, value=password_field).send_keys(password)
    # driver.find_element(by=By.CSS_SELECTOR, value=login_button).click()
    # WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, agree_button)))
    # driver.find_element(by=By.CSS_SELECTOR, value=agree_button).click()
    # WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, alert_popup_close)))
    # driver.find_element(by=By.CSS_SELECTOR, value=alert_popup_close).click()
    # time.sleep(5)
    # WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, billers_button)))
    # driver.find_element(by=By.CSS_SELECTOR, value=billers_button).click()
    # time.sleep(10)
    # # WebDriverWait(driver, 5).until(
    # #     EC.visibility_of_element_located((By.CSS_SELECTOR, filter_criteria_button)))
    # driver.find_element(by=By.CSS_SELECTOR, value=custom_button).click()
    driver.implicitly_wait(10)
    driver.find_element(by=By.CSS_SELECTOR, value=start_date_field).click()
    time.sleep(5)
    driver.implicitly_wait(3)
    driver.find_element(by=By.CSS_SELECTOR, value=start_date_field).send_keys(date)
    driver.implicitly_wait(3)
    driver.find_element(by=By.CSS_SELECTOR, value=end_date_field).click()
    driver.implicitly_wait(3)
    driver.find_element(by=By.CSS_SELECTOR, value=end_date_field).send_keys(date)
    driver.implicitly_wait(3)
    driver.find_element(by=By.CSS_SELECTOR, value=filter_criteria_button).click()
    driver.implicitly_wait(3)
    driver.find_element(by=By.CSS_SELECTOR, value=first_name_button).send_keys(first_name)
    driver.implicitly_wait(3)
    driver.find_element(by=By.CSS_SELECTOR, value=last_name_button).send_keys(last_name)
    driver.implicitly_wait(3)
    driver.find_element(by=By.CSS_SELECTOR, value=mem_button).click()
    driver.implicitly_wait(3)
    driver.find_element(by=By.CSS_SELECTOR, value=superbill_buton).click()
    time.sleep(10)
