import subprocess

# 定义Chrome浏览器的路径
from selenium.webdriver.chrome import webdriver
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
from bit_api import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

# chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome_proxy.exe"
proxy = requests.get("http://192.168.1.198:9049/v1/ips?num=1&country=CA&state=all&city=all&zip=all&t=txt&port=40000&isp=all&start=&end=").text
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# 定义代理服务器的IP地址和端口号
proxy = '192.168.1.198:9049'

# 构建命令行参数
cmd = [
    chrome_path,
    f'--proxy-server={f"{proxy}"}',  # 配置代理服务器
    '--no-first-run',  # 跳过首次运行向导
    '--disable-infobars',  # 禁用Chrome浏览器提示信息条
    '--disable-popup-blocking',  # 禁用弹出窗口拦截
    '--disable-save-password-bubble',  # 禁用保存密码提示气泡
    '--disable-sync-credential-prompt',  # 禁用同步密码提示气泡
    '--force-renderer-accessibility',  # 强制启用无障碍渲染
    '--remote-debugging-port=15000',  # 开启远程调试，设置端口为15000
    '--user-data-dir=C:\\temp\\chrome_data',  # 设置用户数据目录（可选）
    '--start-maximized',  # 启动时最大化窗口
    'https://www.canadiandiamondsclassaction.ca/en/claim/consumer'  # 要打开的网页地址（可选）
]

# 启动Chrome浏览器进程
process = subprocess.Popen(cmd)

chrome_options = webdriver.ChromeOptions()

chrome_options.debugger_address = '192.168.1.198:9049'
chrome_service = Service('Driver/chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.set_page_load_timeout(60)
WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,'//*[@name="purchasedDiamonds" and @value="true"]'))).click()

