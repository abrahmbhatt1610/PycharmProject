import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

executable_path = "/webdrivers"
os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()

chrome_options.add_extension('  Cyber-Ark Clipboard Extension   ')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://empclaims.my.idaptive.app/my#/MyApps")
