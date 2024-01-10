import time
from telnetlib import EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import passRecaptchaV2
from bit_api import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import pyautogui


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", '127.0.0.1:65378')
chrome_service = Service(r'C:\Users\莫冬雷\AppData\Roaming\BitBrowser\chromedriver\112\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.switch_to.default_content()
try:
    frame = driver.find_element(By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]')
except:
    frame = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA 验证将于 2 分钟后过期"]')
driver.switch_to.frame(frame)

# 2Captcha========
def ClickRecaptchaV2(driver):
    questionImagePath = r"D:\CAAutoRegister\question.jpg"
    pcImagePath = r"D:\CAAutoRegister\pc.jpg"
    driver.find_element(By.XPATH, '//strong').screenshot(questionImagePath)
    questionBase64 = driver.find_element(By.XPATH, '//strong').screenshot_as_base64
    driver.find_element(By.XPATH,'//*[@class="rc-imageselect-target"]').screenshot(pcImagePath)
    pcBase64 = driver.find_element(By.XPATH,'//*[@class="rc-imageselect-target"]').screenshot_as_base64
    lenth = len(driver.find_elements(By.XPATH,'//*[@class="rc-image-tile-wrapper"]'))
    elmList = passRecaptchaV2.Towcaptcha(questionBase64,pcBase64,lenth)
    for cliElm in elmList:
        driver.find_elements(By.XPATH, '//*[@class="rc-image-tile-wrapper"]')[cliElm-1].click()
ClickRecaptchaV2(driver)
try:
    driver.find_element(By.XPATH,'//*[text() = "在没有新图片可以点按后，请点击“验证”。"]')
    time.sleep(7)
    ClickRecaptchaV2(driver)
except:
    pass
driver.find_element(By.XPATH,'//*[@class="rc-button-default goog-inline-block"]').click()
time.sleep(2)
try:
    driver.find_element(By.XPATH,'// *[@class ="btn btn-primary"]').click()
except:
    ClickRecaptchaV2(driver)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="rc-button-default goog-inline-block"]').click()

time.sleep(2)
try:
    driver.find_element(By.XPATH, '//*[@class="rc-button-default goog-inline-block"]')
    ClickRecaptchaV2(driver)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="rc-button-default goog-inline-block"]').click()
except:
    pass






