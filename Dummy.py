# grocery = ["Harpic", "vim bar", "deodrant", "Bhindi", "Lollypop", 56]
# # print(grocery)
# numbers = [2, 7, 9, 11, 3]
# # numbers.sort()
# # numbers.reverse()
# print(numbers[1:4])
# numbers.append(5)
# print(numbers)
# var1 = 7
# var2 = 52
# var3 = int(input())
#
# if var3 > var2:
#     print("Greater")
# else:
#     print("Leaser")

import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.ChromiumEdge(EdgeChromiumDriverManager().install())

# url = 'https://empclaims.sharepoint.com/sites/AutomationProjects-Jeannie-Automation/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2Fsites%2FAutomationProjects%2DJeannie%2DAutomation%2FShared%20Documents%2FJeannie%2D%20Automation&FolderCTID=0x0120007D4C87E49F163C48914C87604A6C5414'


# @pytest.fixture()
# def initiate_driver():
#     driver.get("https://empclaims.sharepoint.com/")
#     # driver.get("https://login.advancedmd.com/")
#     driver.maximize_window()
#     time.sleep(10)
#     yield driver
#     driver.close()

a = float(input('Enter first side '))
b = float(input('Enter second side '))
c = float(input('Enter third side '))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
n = (553.4375 ** 0.5)
print(n)
# print(area)
