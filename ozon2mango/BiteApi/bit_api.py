import requests
import json
import time

# 官方文档地址
# https://doc2.bitbrowser.cn/jiekou/ben-di-fu-wu-zhi-nan.html

# 此demo仅作为参考使用，以下使用的指纹参数仅是部分参数，完整参数请参考文档

url = "http://127.0.0.1:54345"
headers = {'Content-Type': 'application/json'}


def createBrowser():  # 创建或者更新窗口，指纹参数 browserFingerPrint 如没有特定需求，只需要指定下内核即可，如果需要更详细的参数，请参考文档
    json_data = {
        'name': 'google',  # 窗口名称
        'remark': '',  # 备注
        'proxyMethod': 2,  # 代理方式 2自定义 3 提取IP
        # 代理类型  ['noproxy', 'http', 'https', 'socks5', 'ssh']
        'proxyType': 'noproxy',
        'host': '',  # 代理主机
        'port': '',  # 代理端口
        'proxyUserName': '',  # 代理账号
        "browserFingerPrint": {  # 指纹对象
            'coreVersion': '112'  # 内核版本 112 | 104，建议使用112，注意，win7/win8/winserver 2012 已经不支持112内核了，无法打开
        }
    }

    res = requests.post(f"{url}/browser/update",
                        data=json.dumps(json_data), headers=headers).json()
    browserId = res['data']['id']
    print(browserId)
    return browserId


def updateBrowser():  # 更新窗口，支持批量更新和按需更新，ids 传入数组，单独更新只传一个id即可，只传入需要修改的字段即可，比如修改备注，具体字段请参考文档，browserFingerPrint指纹对象不修改，则无需传入
    json_data = {'ids': ['93672cf112a044f08b653cab691216f0'],
                 'remark': '我是一个备注', 'browserFingerPrint': {}}
    res = requests.post(f"{url}/browser/update/partial",
                        data=json.dumps(json_data), headers=headers).json()
    print(res)


def openBrowser(id):  # 直接指定ID打开窗口，也可以使用 createBrowser 方法返回的ID
    json_data = {"id": f'{id}'}
    res = requests.post(f"{url}/browser/open",
                        data=json.dumps(json_data), headers=headers).json()
    print(res)
    print(res['data']['http'])
    return res


def closeBrowser(id):  # 关闭窗口
    json_data = {'id': f'{id}'}
    requests.post(f"{url}/browser/close",
                  data=json.dumps(json_data), headers=headers).json()


def deleteBrowser(id):  # 删除窗口
    json_data = {'id': f'{id}'}
    print(requests.post(f"{url}/browser/delete",
          data=json.dumps(json_data), headers=headers).json())


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bit_api import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

def GenCookeis(id):
    # /browser/open 接口会返回 selenium使用的http地址，以及webdriver的path，直接使用即可
    res = openBrowser(f"{id}")
    driverPath = res['data']['driver']
    debuggerAddress = res['data']['http']

    print(driverPath)
    print(debuggerAddress)
    # selenium 连接代码
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", debuggerAddress)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")


    chrome_service = Service(driverPath)
    # driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver = uc.Chrome()

    
    # 导航到网页
    driver.get('https://www.ozon.ru/')
    # 执行一段JavaScript代码
    # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    time.sleep(10)
    

    try:
        # frame=driver.findElement(By.xpath( "//*[@id='cf-chl-widget-wzhw4']" ))
        frame = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/iframe")
        driver.switch_to.frame(frame)
        print("switch to frame success")
        # driver.findElement(By.xpath("//*[@id='challenge-stage']/div/label/input")).click()
        driver.find_element(By.XPATH,"//*[@id='challenge-stage']/div/label/input").click()
    except Exception as e:
        print("发生错误:", e)
        pass

    time.sleep(10)
    # 获取cookies
    cookies = driver.get_cookies()
    print(cookies)





if __name__ == '__main__':
    browser_id = createBrowser()
    openBrowser(browser_id)
    time.sleep(1)
    GenCookeis(browser_id)
    time.sleep(10)  # 等待10秒自动关闭窗口
    closeBrowser(browser_id)
    time.sleep(10)  # 等待10秒自动删掉窗口
    deleteBrowser(browser_id)
