# -*- encoding: utf-8 -*-
'''
@File : address.py
@Time : 2020/04/24 20:31:29
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
#    请查资料，Python的 requests库，如何判断一个网址可以访问；
# 提示 ：使用requests模块
#    def getHtmlText(url):
#     try:        # 网络连接有风险，异常处理很重要
#         r = requests.get(url,timeout=30)    # 查一下这个方法的使用
#         r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#          return "产生异常"

import requests
import threading
from requests.exceptions import RequestException

def getHtmlText(url):
    mutex.acquire()  # 上锁
    try:       
        r = requests.get(url,timeout=30)
        r.encoding = 'gb2312'
        if r.status_code==200:
            print(r.url+':可以访问')
            #return r.text
        else:
            print(url+':不可以访问')
            #return None
    except RequestException:
        print('产生异常')
    mutex.release()  # 解锁

if __name__=='__main__':
    mutex = threading.Lock()
    try:
        with open('F:/Python/homework8/url_data.txt','r')as f:
            for line in f.readlines():
                linesplit=line.split("; ")
                for i in range(len(linesplit)):
                    t = threading.Thread(target=getHtmlText,args=(linesplit[i],))
                    t.start()
    except Exception as error2:
        print(error2)
