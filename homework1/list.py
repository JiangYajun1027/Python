# -*- encoding: utf-8 -*-
'''
@File : list.py
@Time : 2020/03/06 17:45:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#3 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；

list1=[1,3,5,7,9,11,13,15,17,19]
list2=[2,3,5,7,11,13,17,18]
for x in list1:
    for y in list2:
        if x==y:
            print(x,end=' ')
