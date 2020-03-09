# -*- encoding: utf-8 -*-
'''
@File : series.py
@Time : 2020/03/08 22:20:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#6  定义一个函数, 打印输出n以内的斐波那契数列;

def seri(x):
    f1 = 0
    f2 = 1
    for n in range(3,x+1):
        fn = f2 + f1
        if fn<=x:
            print(fn)
            f1,f2 = f2,fn

i=int(input("请输入n的值:"))
seri(i)