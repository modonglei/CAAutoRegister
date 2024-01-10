from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import passRecaptchaV2
from bit_api import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




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
    # f.proxys5.net，6200，35343298-zone-custom-region-US，iOOB7eKW
    browser_id = createLessBrowser()
    # browser_id = createStaticBrowser('http://192.168.1.198:9049/v1/ips?num=1&country=CA&state=all&city=all&zip=all&t=txt&port=40000&isp=all&start=&end=','common')
    # browser_id = createBrowser('f.proxys5.net', 6200, '35343298-zone-custom-region-CA', 'iOOB7eKW')
    res = openBrowser(browser_id)
    driverPath = res['data']['driver']
    debuggerAddress = res['data']['http']
    print(driverPath)
    print(debuggerAddress)
    res = detail(browser_id)
    seq = res['data']['seq']
    time.sleep(1)
    RobotWindowbounds(seq)
    time.sleep(18)
    import pyautogui
    pyautogui.moveTo(x=Points[f'{seq}'][0], y=Points[f'{seq}'][1], duration=0.5)  # 移动鼠标
    pyautogui.click(clicks=1)  # 点击

    time.sleep(80)
    # selenium 连接代码
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", debuggerAddress)
    chrome_options.add_argument('--lang=en_US')
    chrome_service = Service(driverPath)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.set_page_load_timeout(60)
    for i in range(5):
        try:
            WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@name="purchasedDiamonds" and @value="true"]'))).click()
            break
        except:
            driver.refresh()

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@name="confirmResidency" and @value="true"]'))).click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="btn btn-primary"]'))).click()

    # email					  name      	 lastname	   Address         City        Province   PostalCode    Phone     code
    # QHT0GYNL@sdrtdf.com	PATRICIA	CARIGNAN	910 FIFTH AVE	NEW WESTMINSTER	  BC	   V3M 1Y2	     7783977173     1683952
    # S66WBCNY3W@sdrtdf.com	ANDRE	BEDARD	468 RUE SAINT-GERMAIN	QUEBEC	QC	G1K 4N7	4185256701

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[text() = "I am the claimant."]/../input'))).click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="firstName"]'))).send_keys('ANDRE')

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="lastName"]'))).send_keys('BEDARD')

    countrySelect = Select(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="country"]'))))
    countrySelect.select_by_value('Canada')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="address1"]'))).send_keys('468 RUE SAINT-GERMAIN')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="city"]'))).send_keys('QUEBEC')
    #
    provinceSelect = Select(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="province"]'))))
    provinceSelect.select_by_value('QC')
    #
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="postCode"]'))).send_keys(
        'G1K 4N7')
    phoneElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="phone"]')))
    actions = ActionChains(driver)
    actions.move_to_element(phoneElem).click().send_keys("4185256701").perform()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))).send_keys(
        'QHT0GYNL@sdrtdf.com')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email2"]'))).send_keys(
        'QHT0GYNL@sdrtdf.com')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                    '//*[text() = "I do NOT have documentation and wish to claim the Minimum Administrative Payment of $20"]/../input'))).click()
    driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="paymentEmail"]'))).send_keys(
        'QHT0GYNL@sdrtdf.com')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="paymentEmailConfirm"]'))).send_keys('QHT0GYNL@sdrtdf.com')
    birthMonthSelect = Select(
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthMonth"]'))))
    birthMonthSelect.select_by_value('January')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="btn btn-primary"]'))).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirmation"]'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="certification"]'))).click()
    time.sleep(6)
    frame = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
    driver.switch_to.frame(frame)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="recaptcha-checkbox-border"]'))).click()
    time.sleep(7)
    driver.switch_to.default_content()


# 2Captcha========
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
        driver.find_element(By.XPATH, '//*[@class="rc-imageselect-target"]').screenshot(pcImagePath)
        pcBase64 = driver.find_element(By.XPATH, '//*[@class="rc-imageselect-target"]').screenshot_as_base64
        lenth = len(driver.find_elements(By.XPATH, '//*[@class="rc-image-tile-wrapper"]'))
        elmList = passRecaptchaV2.Towcaptcha(questionBase64, pcBase64, lenth)
        for cliElm in elmList:
            driver.find_elements(By.XPATH, '//*[@class="rc-image-tile-wrapper"]')[cliElm - 1].click()

    ClickRecaptchaV2(driver)
    try:
        driver.find_element(By.XPATH, '//*[text() = "在没有新图片可以点按后，请点击“验证”。"]')
        time.sleep(7)
        ClickRecaptchaV2(driver)
    except:
        pass
    driver.find_element(By.XPATH, '//*[@class="rc-button-default goog-inline-block"]').click()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, '// *[@class ="btn btn-primary"]').click()
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

# captchaRun=========
    # question = driver.find_element(By.XPATH, '//strong').text
    # print(question)
    # import passRecaptchaV2
    # passRecaptchaV2.saveImage()
    # time.sleep(4)
    # res = passRecaptchaV2.createTask(question)
    # print(res)

