# -*- encoding: utf-8 -*-
'''
@File : intro.py
@Time : 2020/04/18 16:07:59
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
#     说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#     提示：要用到requests库，BeautifulSoup库

import requests
from bs4 import BeautifulSoup
import re


def getadd():
    listx=[]
    i=1
    with open('F:/Python/homework7/save.txt','r',encoding='utf-8') as f1:
        for line in f1.readlines():
            linesplit=line.split()
            for x in linesplit:
                listx.append(x)
                i=i+1
                if i>100:
                    return listx

def getHtml(listurl,listlabel):
    try:
        linklst = []
        for add in listurl:
            headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
            response = requests.get(add, headers = headers, timeout = 30)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            txt=response.text
            soup = BeautifulSoup(txt, "html.parser")
            label = soup.select("a")
            for x in label:
                if x.string in listlabel:
                    get = x['href']
                    if re.match(r'^http',get):
                        address=get
                    else:
                        address=add+'/'+str(get)
                    print(address)
                    break
        #return linklst
            
    except Exception as error:
        print(error)

if __name__=='__main__':
    listadd=getadd()
    print(listadd)
    print('_______________________________________________________________________________')
    listla=['企业介绍','公司介绍','关于我们','企业发展','公司发展','发展历史','企业概况']
    getHtml(listadd,listla)
    
    
    
    #print('download success!')