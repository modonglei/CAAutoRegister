from selenium import webdriver
from selenium.webdriver.common.by import By

from bit_api import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def runClick(driver,element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

def runSendKeys(driver,element,str):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.send_keys()




def taskRun():
    # Point(x=1935, y=1068) 6
    # Point(x=1035, y=1068) 5
    Points = {
        '1': [135,368],
        '2': [1035,368],
        '3': [1935,368],
        '4': [135,1068],
        '5': [1035,1068],
        '6': [1935,1068]
    }
    # f.proxys5.net:6200:35343298-zone-custom-region-CA:iOOB7eKW
    browser_id = createBrowser('f.proxys5.net', '6200', '35343298-zone-custom-region-CA', 'iOOB7eKW')
    # browser_id = createStaticBrowser('http://192.168.1.198:9049/v1/ips?num=1&country=CA&state=all&city=all&zip=all&t=txt&port=40000&isp=all&start=&end=',
    #                                  'common')
    res = openBrowser(browser_id)
    driverPath = res['data']['driver']
    debuggerAddress = res['data']['http']
    print(driverPath)
    print(debuggerAddress)
    #

    time.sleep(6)
    res = detail(browser_id)
    seq = res['data']['seq']
    time.sleep(1)
    RobotWindowbounds(seq)
    time.sleep(7)
    import pyautogui
    pyautogui.moveTo(x=Points[0], y=Points[1], duration=0.5)  # 移动鼠标
    pyautogui.click(clicks=1)  # 点击

    time.sleep(12)

    # selenium 连接代码
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", debuggerAddress)
    chrome_service = Service(driverPath)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.set_page_load_timeout(60)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@name="purchasedDiamonds" and @value="true"]'))).click()

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@name="confirmResidency" and @value="true"]'))).click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="btn btn-primary"]'))).click()
    #
    # # email					  name      	 lastname	   Address         City        Province   PostalCode    Phone
    # # QHT0GYNL@sdrtdf.com	PATRICIA	CARIGNAN	910 FIFTH AVE	NEW WESTMINSTER	  BC	   V3M 1Y2	     7783977173
    #
    #
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="firstName"]'))).send_keys('PATRICIA')

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="lastName"]'))).send_keys('CARIGNAN')

    countrySelect = Select(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="country"]'))))
    countrySelect.select_by_value('Canada')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="address1"]'))).send_keys('910 FIFTH AVE')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="city"]'))).send_keys('NEW WESTMINSTER')
    #
    provinceSelect = Select(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="province"]'))))
    provinceSelect.select_by_value('BC')
    #
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="postCode"]'))).send_keys('V3M 1Y2')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="phone"]'))).send_keys('7783977173')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="email"]'))).send_keys('QHT0GYNL@sdrtdf.com')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="email2"]'))).send_keys('QHT0GYNL@sdrtdf.com')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="email2"]'))).send_keys('QHT0GYNL@sdrtdf.com')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[text() = "I do NOT have documentation and wish to claim the Minimum Administrative Payment of $20"]/../input'))).click()
