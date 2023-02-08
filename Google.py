import time
from selenium.webdriver.common.by import By

def google_auth(driver, login, password, reserve):
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
               'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
               '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    #driver.implicitly_wait(15)

    loginBox = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
    loginBox.send_keys(login)

    time.sleep(3)

    nextButton = driver.find_elements(By.XPATH, '//*[@id ="identifierNext"]')
    nextButton[0].click()

    time.sleep(5)

    passWordBox = driver.find_element(By.XPATH,
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    passWordBox.send_keys(password)

    time.sleep(3)

    nextButton = driver.find_elements(By.XPATH, '//*[@id ="passwordNext"]')
    nextButton[0].click()

    time.sleep(3)
