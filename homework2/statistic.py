# -*- encoding: utf-8 -*-
'''
@File : statistic.py
@Time : 2020/03/08 18:32:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#4  写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;

def classfy(st):
    letter=0
    num=0
    kong=0
    other=0
    for i in st:
        if i.isalpha():
            letter+=1
        elif i.isdigit():
            num+=1
        elif i.isspace():
            kong+=1
        else:
            other+=1
    return letter,num,kong,other

s=input("请输入字符串:")
print("字母，数字，空格，其他字符的数目为:")
print(classfy(s))
