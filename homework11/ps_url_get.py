#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#给定10万个企业的网址（放在数据库表中），请编写一个网络爬虫，爬取该企业的产品及服务信息（即获取该企业能提供的产品和服务）；
#并将爬取到的数据，保存到数据库中；请自行设计数据库表结构

import requests
from bs4 import BeautifulSoup
import re
import db_query

def getHtml(listlabel):
    try:
        dicx={}
        listx=[]
        for i in range(1,20):
            a,b=db_query.web_query(i)
            b=b.split(';')
            dicx[a]=b[0]
        # print(dicx)

        for a,b in dicx.items():
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
            try:
                response = requests.get(b, headers=headers)
            except:
                print('faild:%s,%s' % (a, b))
                continue
            response.raise_for_status()
            # print(response.status_code)
            response.encoding = response.apparent_encoding
            txt = response.text
            # print(txt)
            soup = BeautifulSoup(txt, "html.parser")
            label = soup.select("a")
            # print(label)
            for x in label:
                if x.string in listlabel:
                    get = x['href']
                    if re.match(r'^http', get):
                        address = get
                    else:
                        address = b + '/' + str(get)
                    # print(address,type(address))
                    listx.append(address)
                    break
        return listx

    except Exception as error:
        print(error)

# def getcon(lis):
#     try:
#         data = []
#         dict = {}
#         headers = {	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
#         for x in lis:
#             test = requests.get(x,headers=headers,timeout = 30).content.decode('utf-8')
#             soup = BeautifulSoup(test,'html.parser')
#
#             # 查找标题
#             dict['title'] = soup.find(id='main').h1.text
#             print(dict['title'])
#
#             # 查找example序号
#             dict['Order'] = soup.find(style="margin:20px 2px; color:#424345; font-weight:bold;").text
#             print(dict['Order'])
#
#             # 查找Project
#             # dict['Project'] = soup.find(id='main').find_all('span')[1].text
#             # print(dict['Project'])
#
#             # 查找Author
#             # dict['Author'] = soup.find(id='content').find_all('p')[2].text
#             # print(dict['Author'])
#
#             # 查找File
#             # dict['File'] = soup.find(id='content').find_all('p')[2].text
#             # print(dict['File'])
#
#             # 程序源代码
#             #这里的异常处理是因为有一部分练习实例存放的位置不一样，然后进行异常处理，不同的情况不一样，根据自己的情况而定！
#             try:
#                 dict['code'] = soup.find('pre',class_="prettyprint").text
#             except Exception as e:
#                 print(e)
#             print(dict['code'])
#             # print(dict)
#
#             with open('F:/Python/homework7/problem.txt','a+',encoding='utf-8') as f:
#                 f.write(dict['title']+'\n')
#                 f.write(dict['Order']+'\n')
#                 f.write(dict['code']+'\n')
#                 f.write('*'*100+'\n')
#                 f.write('\n')
#     except Exception as ex:
#         print(ex)

if __name__ == '__main__':
    listla = ['产品', '主要产品', '产品中心', '产品专区', '产品布局', '产品展示', '产品与服务']
    listlb = ['客户服务', '服务中心', '服务天地', '服务大厅', '疑难业务', '业务领域', '业务范围', '业务介绍', '产业展示']
    print(getHtml(listla))
    print(getHtml(listlb))

    # getcon(url)

    # print('download success!')