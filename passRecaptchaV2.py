import json
import os
from datetime import time

import requests

RecaptchaImagePath = r"D:\CAAutoRegister\payload1.jpg"
points = {
    '1': [219,293],
    '2': [349,293],
    '3': [479,293],
    '4': [219,423],
    '5': [349,423],
    '6': [479,423],
    '7': [219,553],
    '8': [349,553],
    '9': [479,553],
}
def getPoint(seq):
    if seq > 3:
        startY = 700
        startX = 0 + 900 * (seq - 4)
    else:
        startY = 0
        startX = 0 + 900 * (seq - 1)
question_dic = {
  "taxis": "/m/0pg52",
  "bus": "/m/01bjv",
  "school bus": "/m/02yvhj",
  "motorcycles": "/m/04_sv",
  "tractors": "/m/013xlm",
  "chimneys": "/m/01jk_4",
  "crosswalks": "/m/014xcs",
  "traffic lights": "/m/015qff",
  "bicycles": "/m/0199g",
  "parking meters": "/m/015qbp",
  "cars": "/m/0k4j",
  "bridges": "/m/015kr",
  "boats": "/m/019jd",
  "palm trees": "/m/0cdl1",
  "mountains or hills": "/m/09d_r",
  "a fire hydrant": "/m/01pns0",
  "stairs": "/m/01lynh"
}

def createTask(question):

    try:
        question = question_dic[question]
    except KeyError as e:
        print(e)
        return False
    url = 'https://api.captcha.run/v2/tasks'
    headers = {
       'Content-Type': 'application/json',
       'Authorization': 'Bearer b3de4dcb-75f3-4dc2-a4ea-8da656825160'
    }
    import base64
    with open(RecaptchaImagePath, "rb") as image_file:
        imageBase64 = base64.b64encode(image_file.read()).decode('utf-8')
    json_data = {
      "captchaType": "ReCaptchaV2Classification",
      'image': imageBase64,
      'question': question,
      'resize': 0,
      "developer": "e277e73d-f6c7-49ea-a920-4e19166c410a"
    }
    response = requests.post('https://api.captcha.run/v2/tasks', headers=headers, json=json_data).json()
    return response


def saveImage():
    import pyautogui
    import time
    pyautogui.moveTo(points['5'][0],points['5'][1])
    pyautogui.rightClick()
    time.sleep(2)

    import uiautomation as uia
    app1 =uia.PaneControl(ClassName = "Chrome_WidgetWin_1")
    app1.MenuItemControl(Name = "Save image as…").Click()
    time.sleep(2)
    app = uia.WindowControl(Name="另存为")
    app.EditControl(Name = "文件名:").SendKeys(r"D:\CAAutoRegister\payload1.jpg")
    app.ButtonControl(Name="保存(S)").Click()
    time.sleep(1)
    try:
        app = app.PaneControl(Name="确认另存为")
        app.ButtonControl(Name="是(Y)").Click()
    except:
        pass
    timeout = 10  # 等待时间（秒）
    # 判断文件是否存在，如果不存在则循环等待
    start_time = time.time()
    while not os.path.exists(RecaptchaImagePath):
        if time.time() - start_time >= timeout:
            raise Exception("文件下载超时")
        time.sleep(1)  # 每秒检查一次

    # 文件下载完成
    print("文件下载完毕")


def Towcaptcha(questionBase64,pcBase64,lenth):
    import time
    if lenth == 9:
        rows = 3
        columns = 3
    elif lenth == 16:
        rows = 4
        columns = 4
    else:
        rows = 0
        columns = 0
    createUrl = 'https://api.2captcha.com/createTask'
    headers = {'Content-Type': 'application/json'}
    params = {
        "clientKey": "e20e291e758ac3071110407a6a118353",
        "task": {
            "type": "GridTask",
            "body": pcBase64,
            "rows": rows,
            "columns": columns,
            "imgInstructions": questionBase64

        }
    }
    res = requests.post(url=createUrl,data=json.dumps(params),headers=headers).json()
    print(res,type(res))
    taskId = res['taskId']
    indexUrl =  "https://api.2captcha.com/getTaskResult"
    indexparams = {
        "clientKey": "e20e291e758ac3071110407a6a118353",
        "taskId": taskId
    }
    indexRes = requests.post(url=indexUrl, data=json.dumps(indexparams), headers=headers).json()
    print(indexRes)
    for i in range(20):
        if indexRes["errorId"] == 0 and indexRes["status"] == "ready":
            break
        time.sleep(1)
        indexRes = requests.post(url=indexUrl, data=json.dumps(indexparams), headers=headers).json()
        print(indexRes)
    return  indexRes["solution"]["click"]

# Towcaptcha('questionBase64','pcBase64',0)
