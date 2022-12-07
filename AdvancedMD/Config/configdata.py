# from AdvancedMD.Test.TestHomePage import visitid
from AdvancedMD.conftest import initiate_driver

url = ""
# current_url = "https://pm-wfe-102.advancedmd.com/amds/pm/app/index.html#/"

# Valid Credentials
username = "ABRAHMBHATT9"
password = "Empclaims@0123"
office_key = "146705"

# visit_id = "^" + visitid
# print(visit_id)
# visit_id_2 = "8982261"

phe_Code = 'WO PHE'

# Invalid Credentials
invalid_password_number = ""
invalid_username = ""

explicit_wait_time = 10
# implicu?


# import pytest
# from selenium.webdriver.common.by import By
# import time
# from AdvancedMD.LoginPageLocators.HomePageLocators import *
# from AdvancedMD.LoginPageLocators.LoginPageLocators import *
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from AdvancedMD.Config.configdata import *

# from AdvancedMD.conftest import *


# @pytest.mark.usefixture("initiate_driver")
# class TestHomePage:

# def test_verify_HomePage(self, initiate_driver):
# driver = initiate_driver
# driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, login_iframe))
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, login_name)))
# driver.find_element(by=By.CSS_SELECTOR, value=login_name).send_keys(username)
# time.sleep(2)
# driver.find_element(by=By.CSS_SELECTOR, value=password_field).send_keys(password)
# time.sleep(2)
# driver.find_element(by=By.CSS_SELECTOR, value=office_key_field).send_keys(office_key)
# time.sleep(2)
# driver.find_element(by=By.CSS_SELECTOR, value=login_button).click()
# time.sleep(20)
# # WebDriverWait(driver, 10).until(
# #         EC.visibility_of_element_located((By.CSS_SELECTOR, snooze_button)))
# # driver.find_element(by=By.CSS_SELECTOR, value=snooze_button).click()
# driver.switch_to.window(driver.window_handles[1])
# driver.maximize_window()
# time.sleep(10)
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, patient_find_button)))
# driver.find_element(by=By.CSS_SELECTOR, value=patient_find_button).click()
# time.sleep(10)
# driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe1))
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, transaction_history_button)))
# time.sleep(5)
# # driver.implicitly_wait(transaction_history_button, 10)
# driver.find_element(by=By.CSS_SELECTOR, value=transaction_history_button).click()
# time.sleep(3)
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, patient_find_field)))
# time.sleep(10)
# driver.find_element(by=By.CSS_SELECTOR, value=patient_find_field).send_keys(visit_id)
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, patient_click_button)))
# driver.find_element(by=By.CSS_SELECTOR, value=patient_click_button).click()
# time.sleep(20)
# driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe_transaction_history))
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, writeoff_button)))
# driver.find_element(by=By.CSS_SELECTOR, value=writeoff_button).click()
# time.sleep(5)
# driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe_write_off))
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, writeoff_source_button)))
# driver.find_element(by=By.CSS_SELECTOR, value=writeoff_source_button).click()
# text1 = driver.find_element(by=By.CSS_SELECTOR, value=writeoff_source_button).text
# text2 = writeoff_source_button[1]
# print(text1)
# print(text2)
# if writeoff_source_button == "Patient":
#     # driver.find_element(by=By.CSS_SELECTOR, value=cancel_button).click()
#     driver.find_element(by=By.CSS_SELECTOR, value=writeoff_code_field).send_keys(phe_Code)
#     driver.find_element(by=By.CSS_SELECTOR, value=visit_field).send_keys(8982261)
#     time.sleep(10)
