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

# Test Case 5 : Unsuccessful Product creation
def testcase5():
    driver = webdriver.Chrome()
    driver.get("https://localhost:44323/Product/CreateProducts")

    price = driver.find_element(By.ID, "price")
    price.send_keys("dggf")
    print(price.get_attribute("validationMessage"))

    driver.close


# Test Case 7 : Unsuccessful Product Edit
def testcase7():
    driver = webdriver.Chrome()
    driver.get("https://localhost:44323/Product/ProductDetail/1")
    driver.find_element(By.ID, 'update').click()

    productId = driver.find_element(By.XPATH, "//input[@name='ProductId']")
    date = driver.find_element(By.ID,'EffectiveDate')

    try: 
        productId.clear()
        productId.send_keys(4)
        driver.close
        print("Error; Product ID is editable \n")

    except Exception:
        f = open('hello.txt', 'a')
        driver.close
        f.writelines('Product ID is static \n')
        print("Product ID is read only")

    try:
        date.clear()
        driver.close
        print("Error; date of the product is editable \n")
    except Exception:
        f = open('hello.txt', 'a')
        driver.close
        f.writelines('Date is static \n')
        print("Product date is read only")

        

# Test Case 8 : Edit product
def testcase8():
    driver = webdriver.Chrome()
    driver.get("https://localhost:44323/Product/ProductDetail/1")
    driver.find_element(By.ID, 'update').click()

    price = driver.find_element(By.XPATH, "//input[@name='Price']")
    price.clear()
    price.send_keys(140)

    productTitle = driver.find_element(By.ID,'ProductTitle')
    productTitle.clear()
    productTitle.send_keys('Pretty outfit')

    

    try:
        driver.find_element(By.XPATH,
            "//input[@type='submit' and @value='Save']").click()
        driver.save_screenshot("EditSuccessScreenShot.png")
        f = open('hello.txt', 'a')
        f.writelines('Successfull edit \n')
        f.close
        driver.close()
        print("Successfull edit")
    except Exception as e:

        driver.save_screenshot("EditUnSuccessScreenShot.png")
        f = open('hello.txt', 'a')
        f.writelines('Unsccessfull edit:{str(e)} \n')
        f.close
        driver.close()
        print("Unsuccessfull edit")


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
    testcase7()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
