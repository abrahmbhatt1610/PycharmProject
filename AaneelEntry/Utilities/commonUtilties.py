from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.conftest import driver
from selenium.webdriver.support import expected_conditions as EC


class CommonUtil:

    def get_element_text(self, element: str) -> str:
        """
        get text from element
        :param element : string
        """
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
        text = driver.find_element(by=By.CSS_SELECTOR, value=element).text
        return text

    def click_element(self, element):
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
        driver.find_element(by=By.CSS_SELECTOR, value=element).click()