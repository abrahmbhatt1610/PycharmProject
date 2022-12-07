from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from AdvancedMD.LoginPageLocators.HomePageLocators import *
from AdvancedMD.LoginPageLocators.LoginPageLocators import *
from AdvancedMD.conftest import *
from AdvancedMD.Config.configdata import *
from AdvancedMD.Utilities.ExcelData import *


def login_iframe():
    # WebDriverWait(driver, 10).until(
    #     EC.frame_to_be_available_and_switch_to_it(login_iframe))
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, login_iframe)))
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, login_iframe))


def fill_username():
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, login_name)))
    driver.find_element(by=By.CSS_SELECTOR, value=login_name).send_keys(username)


def fill_password():
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, password_field)))
    driver.find_element(by=By.CSS_SELECTOR, value=password_field).send_keys(password)


def fill_office_key():
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, office_key)))
    driver.find_element(by=By.CSS_SELECTOR, value=office_key_field).send_keys(office_key)


def login_button():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(login_button))
    driver.find_element(by=By.CSS_SELECTOR, value=login_button).click()


def perform_login():
    # login_iframe()
    fill_username()
    fill_password()
    fill_office_key()
    login_button()


def window_of_patient_find_field_button():
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))
    driver.maximize_window()
    # driver.switch_to.window(driver.window_handles[1])


def patient_find_button():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(patient_find_button))
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, patient_find_button)))
    driver.find_element(by=By.CSS_SELECTOR, value=patient_find_button).click()


def patient_find_iframe_1():
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(iframe1))


def patient_find():
    window_of_patient_find_field_button()
    patient_find_button()
    patient_find_iframe_1()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(transaction_history_button))
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, transaction_history_button)))
    driver.find_element(by=By.CSS_SELECTOR, value=transaction_history_button).click()


def transaction_history_frame():
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(iframe_transaction_history))


def write_off_process():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(writeoff_button))
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, writeoff_button)))
    driver.find_element(by=By.CSS_SELECTOR, value=writeoff_button).click()


def write_off_frame(self):
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(iframe_write_off))


def perform_write_off(visitid=None):
    write_off_process()
    write_off_frame()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, writeoff_source_button)))
    driver.find_element(by=By.CSS_SELECTOR, value=writeoff_source_button).click()
    source_element = driver.find_elements(by=By.CSS_SELECTOR, value=writeoff_source_button)
    for i in range(len(source_element)):
        Text = source_element[i].text
        if Text == "INSURANCE":
            drop_down = Select(driver.find_element(by=By.CSS_SELECTOR, value=writeoff_source_button))
            drop_down.select_by_visible_text("PATIENT")
            # assert Text == "INSURANCE"
        elif Text == "PATIENT":
            driver.find_element(by=By.CSS_SELECTOR, value=writeoff_code_field).send_keys(phe_Code)
            driver.find_element(by=By.CSS_SELECTOR, value=writeoff_code_field).send_keys(Keys.TAB)
            driver.find_element(by=By.CSS_SELECTOR, value=visit_field).send_keys(visitid)
            driver.find_element(by=By.CSS_SELECTOR, value=visit_field).send_keys(Keys.TAB)
            time.sleep(10)
            amount_webElement = driver.find_elements(by=By.CSS_SELECTOR, value=balance_field)
            entry = driver.find_elements(by=By.CSS_SELECTOR, value=amount_filed)
            assert Text == "PATIENT"
            for e in range(len(amount_webElement)):
                amount = amount_webElement[e].text
                if amount != "0.00":
                    entry[e].send_keys(Keys.BACK_SPACE * 4)
                    entry[e].send_keys(amount)
                    entry[e].send_keys(Keys.TAB)
                    time.sleep(5)
                    driver.find_element(by=By.CSS_SELECTOR, value=ok_buton).click()
                    # assert amount == "0.00"
                else:
                    driver.find_element(by=By.CSS_SELECTOR, value=cancel_button).click()
