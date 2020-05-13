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
    try:        
        data = []
        dict = {}
        headers = {	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
        for x in lis:
            test = requests.get(x,headers=headers,timeout = 30).content.decode('utf-8')
            soup = BeautifulSoup(test,'html.parser')

            # 查找标题
            dict['title'] = soup.find(id='main').h1.text
            print(dict['title'])
            
            # 查找example序号
            dict['Order'] = soup.find(style="margin:20px 2px; color:#424345; font-weight:bold;").text
            print(dict['Order'])

            # 查找Project
            # dict['Project'] = soup.find(id='main').find_all('span')[1].text
            # print(dict['Project'])

            # 查找Author
            # dict['Author'] = soup.find(id='content').find_all('p')[2].text
            # print(dict['Author'])
            
            # 查找File
            # dict['File'] = soup.find(id='content').find_all('p')[2].text
            # print(dict['File'])

            # 程序源代码
            #这里的异常处理是因为有一部分练习实例存放的位置不一样，然后进行异常处理，不同的情况不一样，根据自己的情况而定！
            try:
                dict['code'] = soup.find('pre',class_="prettyprint").text
            except Exception as e:
                print(e)
            print(dict['code'])
            # print(dict)

            with open('F:/Python/homework7/problem.txt','a+',encoding='utf-8') as f:
                f.write(dict['title']+'\n')
                f.write(dict['Order']+'\n')
                f.write(dict['code']+'\n')
                f.write('*'*100+'\n')
                f.write('\n')
    except Exception as ex:
        print(ex)


listurl1=geturl1('https://www.programcreek.com/python/?ClassName=request&submit=Search')
for u in listurl1:
    listurl2=geturl2(u)
    getcon(listurl2)