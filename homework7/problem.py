# -*- encoding: utf-8 -*-
'''
@File : problem.py
@Time : 2020/04/18 16:29:32
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 4 爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；保存到txt文件中（只保留文字）；
#     文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：

import re
import requests
from bs4 import BeautifulSoup
#from urllib import error

def geturl1(url):
    try:
        headers = {	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
        r = requests.get(url,headers=headers,timeout = 30).content.decode('utf-8')
        soup = BeautifulSoup(r,'html.parser')
        a = soup.find_all('a')
        listx = []
        for x in a:
            #print(x.attrs['href'])
            listx.append(x.attrs['href'])
        # for x in listx:
        #     print(x)
        # print('*'*100+'\n')
        listx.pop(0)
        listx.pop(0)
        # for x in listx:
        #     print(x)
        return listx
    except Exception as e:
        print(e)

def geturl2(url):
    try:
        headers = {	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
        r = requests.get(url,headers=headers,timeout = 30).content.decode('utf-8')
        soup = BeautifulSoup(r,'html.parser')
        a = soup.find_all('a')
        listy = []
        for y in a:
            result=re.match(r'https://www.programcreek.com/python/example/[a-zA-Z0-9\.\-\_/]+',y['href'])
            if result:
                listy.append(result.group())
        # for y in listy:
        #     print(y)
        return listy
    except Exception as e:
        print(e)

def getcon(lis):        
    data = []
    
    headers = {	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
    for x in lis:
        test = requests.get(x,headers=headers,timeout = 30).content.decode('utf-8')
        soup = BeautifulSoup(test,'html.parser')
        dict = {}

        # 查找标题
        dict['title'] = soup.find(id='main').h1.text
        print(dict['title'])

        # # 查找题目
        # dict['tm'] = soup_test.find(id='content').find_all('p')[1].text
        # # print(title)

        # # 查找程序分析
        # dict['cxfx'] = soup_test.find(id='content').find_all('p')[2].text
        # # print(cxfx)

        # # 程序源代码
        # #这里的异常处理是因为有一部分练习实例存放的位置不一样，然后进行异常处理，不同的情况不一样，根据自己的情况而定！
        # try:
        #     dict['code'] = soup_test.find(class_="hl-main").text
        # except Exception as e:
        #     dict['code'] = soup_test.find('pre').text
        # # print(code)
        # # print(dict)

        # with open('F:/homework7/problem.txt','a+',encoding='utf-8') as f:
        # f.write('*'*50+'\n')
        # f.write('\n')


listurl1=geturl1('https://www.programcreek.com/python/?ClassName=request&submit=Search')
li=geturl2(listurl1[0])
getcon(li)