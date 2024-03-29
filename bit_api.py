import requests
import json
import time
from logTool import log

# 官方文档地址
# https://doc2.bitbrowser.cn/jiekou/ben-di-fu-wu-zhi-nan.html

# 此demo仅作为参考使用，以下使用的指纹参数仅是部分参数，完整参数请参考文档

url = "http://127.0.0.1:54345"
headers = {'Content-Type': 'application/json'}


def createBrowser(host, port, proxyUserName, proxyPassword):  # 创建或者更新窗口，指纹参数 browserFingerPrint 如没有特定需求，只需要指定下内核即可，如果需要更详细的参数，请参考文档
    json_data = {
        'name': 'google',  # 窗口名称
        'remark': '',  # 备注
        'platform':'https://www.canadiandiamondsclassaction.ca/en/claim/consumer',
        'workbench':'disable',#浏览器窗口工作台页面，localserver 或 disable，默认localserver，不需要显示工作台时，设置disable
        'proxyMethod': 2,  # 代理方式 2自定义 3 提取IP
        # 代理类型  ['noproxy', 'http', 'https', 'socks5', 'ssh']
        'disableTranslatePopup':'true',#禁止谷歌翻译弹出
        'isIpCreateDisplayLanguage':'true',#是否基于ip生成对应浏览器界面
        'proxyType': 'socks5',
        'host': host,  # 代理主机
        'port': port,  # 代理端口
        'proxyUserName': proxyUserName,  # 代理账号
        'proxyPassword': proxyPassword,
        "browserFingerPrint": {  # 指纹对象
            'isIpCreateDisplayLanguage': 'true',#是否基于IP生成对应国家的浏览器界面语言
            'isIpCreateTimeZone': 'true', #基于IP生成对应的时区
            'webRTC': '2', # webrtc 0替换 | 1允许 | 2禁止
            'isIpCreatePosition': 'true', # 是否基于IP生成对应的地理位置
            'version': '109',   #浏览器版本，不填则随机
            'coreVersion': '112'  # 内核版本 112 | 104，建议使用112，注意，win7/win8/winserver 2012 已经不支持112内核了，无法打开
        }
    }
    res = requests.post(f"{url}/browser/update",
                        data=json.dumps(json_data), headers=headers).json()
    browserId = res['data']['id']
    log.info(f'browserId:{browserId}')
    return browserId
def createLessBrowser():  # 创建或者更新窗口，指纹参数 browserFingerPrint 如没有特定需求，只需要指定下内核即可，如果需要更详细的参数，请参考文档
    json_data = {
        'name': 'google',  # 窗口名称
        'remark': '',  # 备注
        'platform':'https://www.canadiandiamondsclassaction.ca/en/claim/consumer',
        'workbench':'disable',#浏览器窗口工作台页面，localserver 或 disable，默认localserver，不需要显示工作台时，设置disable
        'proxyMethod': 2,  # 代理方式 2自定义 3 提取IP
        # 代理类型  ['noproxy', 'http', 'https', 'socks5', 'ssh']
        'disableTranslatePopup':'true',#禁止谷歌翻译弹出
        'isIpCreateDisplayLanguage':'true',#是否基于ip生成对应浏览器界面
        'proxyType': 'noproxy',
        # 'host': host,  # 代理主机
        # 'port': port,  # 代理端口
        # 'proxyUserName': proxyUserName,  # 代理账号
        # 'proxyPassword': proxyPassword,
        "browserFingerPrint": {  # 指纹对象
            'isIpCreateLanguage': 'false',
            'languages': 'en-US',
            'isIpCreateTimeZone': 'true', #基于IP生成对应的时区
            'webRTC': '2', # webrtc 0替换 | 1允许 | 2禁止
            'isIpCreatePosition': 'true', # 是否基于IP生成对应的地理位置
            'version': '109',   #浏览器版本，不填则随机
            'coreVersion': '112'  # 内核版本 112 | 104，建议使用112，注意，win7/win8/winserver 2012 已经不支持112内核了，无法打开
        }
    }
    res = requests.post(f"{url}/browser/update",
                        data=json.dumps(json_data), headers=headers).json()
    browserId = res['data']['id']
    log.info(f'browserId:{browserId}')
    return browserId

def createStaticBrowser(dynamicIpUrl,dynamicIpChannel):  # 创建或者更新窗口，指纹参数 browserFingerPrint 如没有特定需求，只需要指定下内核即可，如果需要更详细的参数，请参考文档
    json_data = {
        'name': 'google',  # 窗口名称
        'platform': 'https://www.canadiandiamondsclassaction.ca/en/claim/consumer',
        'remark': '',  # 备注
        'proxyMethod': 3,  # 代理方式 2自定义 3 提取IP
        # 代理类型  ['noproxy', 'http', 'https', 'socks5', 'ssh']
        'proxyType': 'socks5',
        'dynamicIpUrl': dynamicIpUrl,  # proxyMethod = 3时，提取IP链接
        'dynamicIpChannel': dynamicIpChannel,  # 提取链接服务商，rola | doveip | cloudam | common
        'isDynamicIpChangeIp': 'true',  # 提取IP，每次打开都提取新IP，默认false
        'duplicateCheck': 1,  # 提取IP校验重复，1 校验，0 不校验。打开窗口时，将检测提取IP是否重复，重复则重新提取，最多重新提取5次
        "browserFingerPrint": {  # 指纹对象
            'isIpCreateDisplayLanguage': 'true',#是否基于IP生成对应国家的浏览器界面语言
            'isIpCreateTimeZone': 'true', #基于IP生成对应的时区
            'webRTC': '2', # webrtc 0替换 | 1允许 | 2禁止
            'isIpCreatePosition': 'true', # 是否基于IP生成对应的地理位置
            'version': '109',   #浏览器版本，不填则随机
            'coreVersion': '112'  # 内核版本 112 | 104，建议使用112，注意，win7/win8/winserver 2012 已经不支持112内核了，无法打开
        }
    }
    res = requests.post(f"{url}/browser/update",
                        data=json.dumps(json_data), headers=headers).json()
    browserId = res['data']['id']
    log.info(f'browserId:{browserId}')
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
    log.info(res)
    log.info(res['data']['http'])
    return res


def closeBrowser(id):  # 关闭窗口
    json_data = {'id': f'{id}', 'queue': 'true'}
    requests.post(f"{url}/browser/close",
                  data=json.dumps(json_data), headers=headers).json()


def deleteBrowser(id):  # 删除窗口
    json_data = {'id': f'{id}'}
    print(requests.post(f"{url}/browser/delete",
          data=json.dumps(json_data), headers=headers).json())

def flexable(seqlist): #一键自适应排列窗口 seqlist要排列的窗口序号数组，不传则排列全部
    json_data = {"seqlist": f'{seqlist}'}
    print(requests.post(f"{url}/windowbounds/flexable",
                  data=json.dumps(json_data), headers=headers).json())

def windowbounds(width,height,col,seqlist=[]): #排列窗口以及调整窗口尺寸,参数除了type，其他参数类型都必须是整型数字
    json_data = {
          "type": "box", # 排列方式，宫格 box ， 对角线 diagonal
          "startX": 0, # 起始X位置
          "startY": 0, # 起始Y位置
          "width": width, # 宽度
          "height": height, # 高度
          "col": col, # 宫格排列时，每行列数
          "spaceX": 0, # 宫格横向间距
          "spaceY": 0, # 宫格纵向间距
          "offsetX": 50, # 对角线横向偏移量
          "offsetY": 50,# 对角线纵向偏移量
          "seqlist": [] #序号数组,要排列的窗口序号数组，不传则排列全部
        }
    print(requests.post(f"{url}/windowbounds",
                  data=json.dumps(json_data), headers=headers).json())

def RobotWindowbounds(seq): #排列窗口以及调整窗口尺寸,参数除了type，其他参数类型都必须是整型数字
    seqlist = []
    seqlist.insert(0,seq)
    if seq > 3:
        startY = 700
        startX = 0 + 900 * (seq - 4)
    else:
        startY = 0
        startX = 0 + 900 * (seq - 1)
    json_data = {
      "type": "box", # 排列方式，宫格 box ， 对角线 diagonal
      "startX": startX, # 起始X位置
      "startY": startY, # 起始Y位置
      "width": 900, # 宽度
      "height": 700, # 高度
      "col": 1, # 宫格排列时，每行列数
      "spaceX": 0, # 宫格横向间距
      "spaceY": 0, # 宫格纵向间距
      "offsetX": 50, # 对角线横向偏移量
      "offsetY": 50,# 对角线纵向偏移量
      "seqlist": seqlist #序号数组,要排列的窗口序号数组，不传则排列全部
    }
    print(requests.post(f"{url}/windowbounds",
                  data=json.dumps(json_data), headers=headers).json())

def detail(id):  # 获取浏览器窗口详情
    json_data = {
        "id": id
    }
    res = requests.post(f"{url}/browser/detail",
                        data=json.dumps(json_data), headers=headers).json()
    print(res)
    return res

def ports():  # 获取浏览器窗口详情
    json_data = {
    }
    res = requests.post(f"{url}/browser/ports",
                        data=json.dumps(json_data), headers=headers).json()
    print(res)
    return res

if __name__ == '__main__':
    # RobotWindowbounds(1)
    # RobotWindowbounds(2)
    # RobotWindowbounds(3)
    # RobotWindowbounds(4)
    # RobotWindowbounds(5)
    # RobotWindowbounds(6)
    # RobotWindowbounds(7)
    id = list(ports()["data"].keys())[0]
    id1 = '485d60f7b7374808a5951524207efc22'
    # id2 = 'c30416718d444076bc02ed1c11afaa89'
    # id3 = 'b869b02861854d08a8d7c110df25d08b'
    closeBrowser(id)
    deleteBrowser(id)
    # closeBrowser(id1)
    # deleteBrowser(id1)
    # closeBrowser(id2)
    # deleteBrowser(id2)
    # res = detail(id)
    # res1 = detail(id1)
    # RobotWindowbounds([7])
    ports()
    # detail(id)
