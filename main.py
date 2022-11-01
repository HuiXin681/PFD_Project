from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    chrmDriver = webdriver.Chrome()
    chrmDriver.get("https://localhost:44323")

    # Find elements in login page & enter test case

    # Test Case 1 : Login 
    username = chrmDriver.find_element(By.ID, 'uname')
    username.send_keys('ProductManager')
    password = chrmDriver.find_element(By.ID, 'upass')
    password.send_keys('passProduct')
    chrmDriver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']").click()

    # Test Case 4 : Obsolete button
    chrmDriver.find_element(By.XPATH, "//input[@type='submit' and @value='Obsolete']").click()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
