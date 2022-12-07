import time
import pytest
from selenium.webdriver.common.by import By
from AaneelEntry.Locators.HomePageLocators import *
from AaneelEntry.Locators.LoginPageLocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from AaneelEntry.Config.configdata import *
from AaneelEntry.Utilities.Exce_Data import *
import pandas as pd


@pytest.mark.usefixture("initiate_driver")
class TestHomePage:

    def test_verify_HomePage(self, initiate_driver):
        driver = initiate_driver
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, username_field)))
        driver.find_element(by=By.CSS_SELECTOR, value=username_field).send_keys(username)
        driver.find_element(by=By.CSS_SELECTOR, value=password_field).send_keys(password)
        driver.find_element(by=By.CSS_SELECTOR, value=login_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, agree_button)))
        driver.find_element(by=By.CSS_SELECTOR, value=agree_button).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, alert_popup_close)))
        driver.find_element(by=By.CSS_SELECTOR, value=alert_popup_close).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, schedule_button)))
        driver.find_element(by=By.CSS_SELECTOR, value=schedule_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, billers_button)))
        '''This will check for the "Billers Review tab"'''
        driver.find_element(by=By.CSS_SELECTOR, value=billers_button).click()
        time.sleep(10)
        driver.find_element(by=By.CSS_SELECTOR, value=filter_criteria_button).click()
        driver.implicitly_wait(3)
        driver.find_element(by=By.CSS_SELECTOR, value=total_button).click()
        driver.find_element(by=By.CSS_SELECTOR, value=select_none_button).click()
        driver.find_element(by=By.CSS_SELECTOR, value=filter_criteria_button).click()
        driver.implicitly_wait(3)
        # WebDriverWait(driver, 5).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, filter_criteria_button)))
        '''Need to select custom button for adding the  Date of Service from Excel'''
        driver.find_element(by=By.CSS_SELECTOR, value=custom_button).click()
        driver.implicitly_wait(3)
        time.sleep(3)
        for row in range(df.shape[0]):
            patient_last_name = df.at[row, "Patient last name"]
            patient_first_name = df.at[row, "PatientFirstname"]
            appoint_date = df.at[row, "Appointment"].strftime('%m/%d/%Y')


            # print(patient_first_name, patient_last_name, appoint_date)

            '''We need to add date of service. 
            start_date_field and end_date_field must be same to find correct date of service of the patient '''
            driver.find_element(by=By.CSS_SELECTOR, value=start_date_field).click()
            driver.find_element(by=By.CSS_SELECTOR, value=start_date_field).send_keys(Keys.BACK_SPACE * 10)
            driver.implicitly_wait(3)
            time.sleep(3)
            driver.find_element(by=By.CSS_SELECTOR, value=start_date_field).send_keys(appoint_date)
            driver.implicitly_wait(3)
            time.sleep(3)
            # ActionChains.send_keys(Keys.TAB)
            driver.find_element(by=By.CSS_SELECTOR, value=end_date_field).click()
            driver.find_element(by=By.CSS_SELECTOR, value=end_date_field).send_keys(Keys.BACK_SPACE * 10)
            driver.implicitly_wait(3)
            time.sleep(3)
            driver.find_element(by=By.CSS_SELECTOR, value=end_date_field).send_keys(appoint_date)
            driver.implicitly_wait(3)
            time.sleep(3)
            # ActionChains.send_keys(Keys.TAB)
            '''Please click filter criteria for add the name of the patient'''
            driver.find_element(by=By.CSS_SELECTOR, value=filter_criteria_button).click()
            driver.implicitly_wait(3)
            time.sleep(3)
            '''Add patient first name '''
            driver.find_element(by=By.CSS_SELECTOR, value=first_name_button).clear()
            # time.sleep(2)
            driver.find_element(by=By.CSS_SELECTOR, value=first_name_button).send_keys(patient_first_name)
            driver.implicitly_wait(3)
            time.sleep(3)
            '''Add patient last name '''
            driver.find_element(by=By.CSS_SELECTOR, value=last_name_button).clear()
            driver.find_element(by=By.CSS_SELECTOR, value=last_name_button).send_keys(patient_last_name)
            driver.implicitly_wait(3)
            time.sleep(3)
            '''click on Mem button for getting the same patient again after switching back from another window'''
            driver.find_element(by=By.CSS_SELECTOR, value=mem_button).click()
            driver.implicitly_wait(3)
            time.sleep(3)
            # name = (last_name + " , " + first_name)
            # assert text_value == name
            '''
            select supper-bill button for adding the details of the patient
            this will open another window
            '''
            driver.find_element(by=By.CSS_SELECTOR, value=superbill_buton).click()
            time.sleep(3)
            driver.find_element(by=By.CSS_SELECTOR, value=back_button).click()
            time.sleep(6)
            # driver.find_element(by=By.CSS_SELECTOR, value=user_log_out_name).click()
            # time.sleep(2)
            # driver.find_element(by=By.CSS_SELECTOR, value=log_out).click()
