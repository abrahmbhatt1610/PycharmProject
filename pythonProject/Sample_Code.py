from re import search

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def initiate_chrome_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())


def test_search_functionality_of_amazon_search_field():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.com")
    driver.maximize_window()
    search_box = driver.find_element(by=By.CSS_SELECTOR, value="#twotabsearchtextbox")

    # print(driver.find_element(by=By.CSS_SELECTOR, value="#twotabsearchtextbox"))
    search_term = ["Pen", "Toy","Chocolate" ]
    search_box.send_keys(search_term)
    magnifier_icon = driver.find_element(by=By.CSS_SELECTOR, value="#nav-search-submit-button")
    magnifier_icon.click()

    list_of_product = driver.find_elements(by=By.CSS_SELECTOR, value=".a-size-mini.a-spacing-none.a-color-base.s-line-clamp-3")
    for i in list_of_product:
        print(i.text)
        assert search_term in i.text, "Keyword not found"

    import time

    time.sleep(10)

    driver.quit()


test_search_functionality_of_amazon_search_field()

'''
1. unittest
2. Nose
3. Pytest
 find 50 safty locater
 '''
