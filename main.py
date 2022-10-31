from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    chrmDriver = webdriver.Chrome()
    chrmDriver.get("https://localhost:44323/Product/ProductDetail/2")

    # Find elements in login page & enter test case

    # Test Case 1 : Login 
    username = chrmDriver.find_element(By.ID, 'uname')
    username.send_keys('ProductManager')
    password = chrmDriver.find_element(By.ID, 'upass')
    password.send_keys('passProduct')
    submitBtn = chrmDriver.find_element(By.ID, 'submitBtn')
    submitBtn.send_keys(Keys.ENTER)

    # Test Case 4 : Obsolete button
    obsoleteBtn = chrmDriver.find_element(By.ID, 'obsoleteBtn')
    obsoleteBtn.send_keys(Keys.ENTER)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
