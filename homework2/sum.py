# -*- encoding: utf-8 -*-
'''
@File : sum.py
@Time : 2020/03/08 17:34:35
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


 #2 编写一个函数,接收n个数字，求这些参数数字的和;

def sum_(L):
    total=0
    for i in L:
        total+=i
    return total
list_=[]
for x in range(5):
    list_.append(int(input("请输入元素:")))
print(sum_(list))
