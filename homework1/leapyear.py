# -*- encoding: utf-8 -*-
'''
@File : leapyear.py
@Time : 2020/03/07 15:43:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#判断用户输入的年份是否为闰年

year=int(input("请输入年份:"))
if year%400==0:
    print("是闰年")
elif year%4==0 and year%100!=0:
    print("是闰年")
else:
    print("不是闰年")
