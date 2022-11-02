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
    try:
        chrmDriver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit123']").click()
        chrmDriver.save_screenshot("LoginSuccessScreenshot.png")
        f = open('hello.txt', 'a')
        f.writelines('Successful login \n')
        f.close()
        chrmDriver.close()
        print("Successful login")
    except Exception as e:
        chrmDriver.save_screenshot("LoginUnsuccessfulScreenshot.png")
        f = open('hello.txt', 'a')
        f.writelines(f'Unsuccessful login error:{str(e)} \n')
        f.close()
        chrmDriver.close()
        print('Unsuccessful login')

# Test Case 4 : Obsolete button
def testcase4():
    chrmDriver = webdriver.Chrome()
    chrmDriver.get("https://localhost:44323/Product/ProductDetail/1")
    try:
        Obsolete = chrmDriver.find_element(By.XPATH, "//input[@value='Obsolete' and @class= 'btn btn-primary']")
        Obsolete.send_keys(Keys.ENTER)
        chrmDriver.save_screenshot("obsoletesuccessfulScreenshot.png")
        f = open('hello.txt', 'a')
        f.writelines('Successful Clicking Obsolete \n')
        f.close()
        chrmDriver.close()
        print("Successful Clicking Obsolete")
        chrmDriver.close()
    except Exception as e:
        chrmDriver.save_screenshot("obsoleteUnsuccessfulScreenshot.png")
        f = open('hello.txt', 'a')
        f.writelines(f'Unsuccessful clicking obsolete:{str(e)} \n ')
        f.close()
        chrmDriver.close()
        print('Unsuccessful Clicking Obsolete ')


if __name__ == '__main__':
    testcase1()
    testcase4()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
