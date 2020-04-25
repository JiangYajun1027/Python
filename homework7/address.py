# -*- encoding: utf-8 -*-
'''
@File : address.py
@Time : 2020/04/18 12:01:43
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
#   提示，文件有10000行，注意控制每次读取的行数；

import re

def readtxt():
    i=1
    with open('F:/Python/homework7/webspiderUrl.txt','r',encoding="utf-8") as f1:
        with open('F:/Python/homework7/save.txt','a+',encoding="utf-8") as f2:
            for line in f1.readlines():
                ret=re.findall(r'http://[a-zA-Z0-9\.\-\u4e00-\u9fa5]+',line)
                if ret:
                    for x in ret:
                        f2.write(x+'     ')
                    f2.write('\n')
                    i=i+1
                else:
                    print('%d:'%i+'null')
                    i=i+1

if __name__ == "__main__":
    readtxt()
