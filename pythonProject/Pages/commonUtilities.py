import time

from select import select
from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

from Pages.HomepageLocaters import sign_in_button
from Pages.LoginPageLocaters import email_field, continue_button, password_button, all_selection_dropdown
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as ac, ActionChains
driver = webdriver.Chrome(ChromeDriverManager().install())

class Commonutil:
    def get_element_text(self, element):
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(By.CSS_SELECTOR))