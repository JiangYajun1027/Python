# -*- encoding: utf-8 -*-
'''
@File : ipdress.py
@Time : 2020/03/30 10:07:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip

import random

ip=['172.25.254.'+str(x) for x in range(1,255)]
with open('F:/Python/homework4/ip.txt','a+',encoding='utf-8')as f1:
    for i in range(0,1200):
        f1.write(random.sample(ip,1)[0]+'\n')

ipdic={}
with open('F:/Python/homework4/ip.txt','r',encoding='utf-8')as f2:
    for x in f2.readlines():
        x=x.strip()
        if x in ipdic:
            ipdic[x]+=1
        else:
            ipdic[x]=1
sortedipdic=sorted(ipdic.items(),key=lambda  x:x[1],reverse=True)

count=0
for x in sortedipdic:
    if count==10:
        break
    else:
        print("%s\t%s\n"%(x[0],x[1]))
        count+=1
        