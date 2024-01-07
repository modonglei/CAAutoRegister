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
from bit_api import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
# selenium 连接代码
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", '127.0.0.1:64130')
chrome_service = Service(r'C:\Users\莫冬雷\AppData\Roaming\BitBrowser\chromedriver\112\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


# Point(x=926, y=357)
import pyautogui as gui
time.sleep(3)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe')))
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="ctp-checkbox-label"]'))).screenshot('img/bb.jpg')








def checkbox():
    # time.sleep(8)
    # driver.switch_to.default_content()
    # time.sleep(1)
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@class="ctp-checkbox-label"]')))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="ctp-checkbox-label"]'))).click()
    # checkbox = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@type="checkbox"]')))
    # ActionChains(driver).move_to_element(checkbox).pause(0.5).click().release().perform()
    # time.sleep(12)
# checkbox()
# for i in range(5):
#     try:
#         WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@name="purchasedDiamonds" and @value="true"]'))).click()
#         break
#     except:
#         driver.refresh()
#         time.sleep(4)
#         checkbox()
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@name="confirmResidency" and @value="true"]'))).click()
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="btn btn-primary"]'))).click()
# #
# # # email					  name      	 lastname	   Address         City        Province   PostalCode    Phone
# # # QHT0GYNL@sdrtdf.com	PATRICIA	CARIGNAN	910 FIFTH AVE	NEW WESTMINSTER	  BC	   V3M 1Y2	     7783977173
# #
# #
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="btn btn-primary"]'))).send_keys('PATRICIA')
#
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="lastName"]'))).send_keys('CARIGNAN')
#
# countrySelect = Select(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="country"]'))))
# countrySelect.select_by_value('Canada')
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="address1"]'))).send_keys('910 FIFTH AVE')
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="city"]'))).send_keys('NEW WESTMINSTER')
# #
# provinceSelect = Select(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="province"]'))))
# provinceSelect.select_by_value('BC')
# #
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="postCode"]'))).send_keys('V3M 1Y2')
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="phone"]'))).send_keys('7783977173')
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="email"]'))).send_keys('QHT0GYNL@sdrtdf.com')
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="email2"]'))).send_keys('QHT0GYNL@sdrtdf.com')
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="email2"]'))).send_keys('QHT0GYNL@sdrtdf.com')
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[text() = "I do NOT have documentation and wish to claim the Minimum Administrative Payment of $20"]/../input'))).click()
