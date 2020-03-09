# -*- encoding: utf-8 -*-
'''
@File : sort.py
@Time : 2020/03/09 18:54:55
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#9  定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);

def sort_(list_):
    list1=sorted(list_)
    print(list1)

x=eval(input("请输入一个数组:"))
sort_(x)