# -*- coding: UTF-8 -*-
import requests, re, time, random, threading
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


cookies = requests.cookies.RequestsCookieJar()
cookies.set("language", "cn_CN", domain=".p06.rocks", path="/")

#--------------------------------------
# 91 的临时站点，可以随时更换
#URL = "http://91porn.com/"
#URL = "http://91.91p17.space/"
#URL = "https://p06.rocks"
# 用HTTP协议
URL = "http://807.workgreat17.live/"
KEY = "91"
KEY_SRC = "91_src" # 每个视频源url对于的redis key
KEY_NONE = "91_none"
#----------------------------------------
import os


'''
  获取访问的主页面
'''
def getNumber():
    r = 0
    while True:
        num = input("请输入你想抓取的总页数:")
        try:
            r = int(num)
            break
        except:
            print("抱歉，您输入的不是有效的数字, 请重新输入.")
            continue
    return r

'''
  获取时长
'''
def getTime():
    r = 0
    while True:
        num = input("请输入想获取的时长(分钟):")
        try:
            r = int(num)
            break
        except:
            print("抱歉，您输入的不是有效的数字, 请重新输入.")
            continue
    return r

'''
   构造随机ip作为请求头访问目标站点
'''
def visit(url):
    randomIP = str(random.randint(0, 255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
    retries = Retry(total=5,backoff_factor=10, status_forcelist=[500,502,503,504])
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',"Accept-Language":"zh-CN,zh;",
        'X-Forwarded-For': randomIP}
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=retries))
    html = s.get(url, headers=headers, cookies=cookies, stream=True).content
    return html