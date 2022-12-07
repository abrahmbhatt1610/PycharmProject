import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from AdvancedMD.LoginPageLocators.HomePageLocators import *
from AdvancedMD.LoginPageLocators.LoginPageLocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from AdvancedMD.Config.configdata import *
from AdvancedMD.Utilities.ExcelData import *
# from AdvancedMD.Utilities.LoginPageUtilities import *
from selenium.webdriver.common.action_chains import ActionChains
from AdvancedMD.conftest import *


@pytest.mark.usefixture("initiate_driver")
class TestHomePage:

    def test_verify_HomePage(self, initiate_driver):
        # driver = initiate_driver
        driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, login_iframe))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, login_name)))
        driver.find_element(by=By.CSS_SELECTOR, value=login_name).send_keys(username)
        time.sleep(2)
        driver.find_element(by=By.CSS_SELECTOR, value=password_field).send_keys(password)
        time.sleep(2)
        driver.find_element(by=By.CSS_SELECTOR, value=office_key_field).send_keys(office_key)
        time.sleep(2)
        driver.find_element(by=By.CSS_SELECTOR, value=login_button).click()
        time.sleep(20)
        driver.switch_to.window(driver.window_handles[1])
        driver.maximize_window()
        time.sleep(10)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, patient_find_button)))
        driver.find_element(by=By.CSS_SELECTOR, value=patient_find_button).click()
        time.sleep(10)
        driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe1))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, transaction_history_button)))
        driver.find_element(by=By.CSS_SELECTOR, value=transaction_history_button).click()
        time.sleep(3)

        for data in x:
            time.sleep(3)
            visitid = data
            visit_id = "^" + str(visitid)
            # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, patient_find_field)))
            time.sleep(10)
            driver.find_element(by=By.XPATH, value=patient_find_field).send_keys(visit_id)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, patient_click_button)))
            driver.find_element(by=By.CSS_SELECTOR, value=patient_click_button).click()
            time.sleep(5)
            driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe_transaction_history))
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, writeoff_button)))
            driver.find_element(by=By.CSS_SELECTOR, value=writeoff_button).click()
            time.sleep(5)
            driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe_write_off))
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
                break
            driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe_transaction_history))
        driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe1))

    # driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe1))

    # assert text == "PATIENT"
    # assert amount == 43.94
