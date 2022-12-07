import time

from select import select
from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from Pages.HomepageLocaters import sign_in_button
from Pages.LoginPageLocaters import email_field, continue_button, password_button, all_selection_dropdown
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as ac, ActionChains

#password_mine = "amrish@1610"



class TestLoginPage:

    # def perform_login(self, username, password):


    @pytest.mark.usefixture("initiate_driver")
    def test_verify_login_with_wrong_credentials(self, initiate_driver):
        driver = initiate_driver
        dropdown = driver.find_elements(by=By.CSS_SELECTOR, value=all_selection_dropdown)
        # select_button.click()
        select_element = Select(driver.find_element(by=By.CSS_SELECTOR, value=all_selection_dropdown))
        select_element.select_by_value("search-alias=arts-crafts-intl-ship")
        time.sleep(10)
        # sign_button = driver.find_element(by=By.CSS_SELECTOR, value=sign_in_button)
        # sign_button.click()
        # ac = ActionChains(driver)
        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located(all_selection_dropdown))



    #
    #
    #
    #     email_field_find= driver.find_element(by=By.CSS_SELECTOR, value=email_field).send_keys(7984879566)
    #     time.sleep(5)
    #     continue_button_find = driver.find_element(by=By.CSS_SELECTOR, value= continue_button).click()
    #     time.sleep(5)
        #email_field.sendkeys("7984879566")
        #continue_button.click()
        #password_button.click()
        #password_button.sendkeys("1610")
    # @pytest.mark.usefixtures("initiate_drvier")
    # def test_verify_user_should_be_navgate_amazon_india_page(self, initiate_driver):
    #     driver = initiate_driver
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.CSS_SELECTOR, email_field))
    #     tabs = driver.window_handles
    #     print(tabs)
    #     driver.find_element(By.CSS_SELECTOR, email_field).click()

        #
        # driver.switch_to.frame()
        # driver.switch_to.alert.dismiss()
    # @pytest.mark.usefixtures("initiate driver")
    # def test_verify_working_with_dropdown_on_amazon_homepage(self, initiate_driver):
    #     driver = initiate_driver
    #     driver.get("https://www.amazon.in")
    #     # WebDriverWait(driver, 10).until(
    #     #     EC.visibility_of_element_located(By.CSS_SELECTOR, all_selection_drop_down))





