from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Test Case 1 : Login
def testcase1():
    chrmDriver = webdriver.Chrome()
    chrmDriver.get("https://localhost:44323")

    # Find elements in login page & enter test case
    username = chrmDriver.find_element(By.ID, 'uname')
    username.send_keys('ProductManager')
    password = chrmDriver.find_element(By.ID, 'upass')
    password.send_keys('passProduct')
    chrmDriver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']").click()
    print("Successful Login")


# Test Case 4 : Obsolete button
def testcase4():
    chrmDriver = webdriver.Chrome()
    chrmDriver.get("https://localhost:44323/Product/ProductDetail/1")
    Obsolete = chrmDriver.find_element(By.XPATH, "//input[@value='Obsolete' and @class= 'btn btn-primary']")
    Obsolete.send_keys(Keys.ENTER)
    print("Successful Clicking Obsolete")
    chrmDriver.close()


if __name__ == '__main__':
    testcase1();
    testcase4();


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
