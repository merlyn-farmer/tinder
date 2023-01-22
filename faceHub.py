from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from info import create_profile
from info import create_driver


import pyautogui as pg
import os

def facehub(driver):
    driver.get("https://facehub.live/home/free-swap-image")
    time.sleep(15)
    driver.find_element(By.XPATH, "//div[normalize-space()='File Requirements']").click()
    os.startfile("focus.exe")
    time.sleep(3)
    pg.write("C:\\test\\1.jpg")
    time.sleep(0.2)
    pg.press("enter")
    time.sleep(15)
    driver.find_element(By.XPATH, "//div[@class='form-btn model-select ant-dropdown-button mouse-hover ant-dropdown-trigger']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[normalize-space()='Pro Mode']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class='swap-form-redirect']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[normalize-space()='Upload']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[normalize-space()='Character']").click()
    os.startfile("focus.exe")
    time.sleep(3)
    pg.write("C:\\test\\2.jpg")
    time.sleep(0.2)
    pg.press("enter")
    time.sleep(15)
    driver.find_element(By.XPATH, "//div[@class='avatar-tabs']//div[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='face-src-select face-srcs']//div[1]//img[1]").click()
    time.sleep(6)
    pg.click("FaceSwap.png")
    time.sleep(15)
    pg.click("agree.png")
    time.sleep(15)
    driver.find_element(By.XPATH, "//div[@class='image-single loading-image hover-enable']//div[@class='loading-content']").click()
    time.sleep(2)
    pg.click("download.png")