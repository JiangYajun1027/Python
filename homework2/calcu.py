# -*- encoding: utf-8 -*-
'''
@File : calcu.py
@Time : 2020/03/09 19:08:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#10 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)

def calculate(x,y,z):
    if y=='+':
        return x+z
    elif y=='-':
        return x-z
    elif y=='*':
        return x*z
    else:
        return x/z

a=float(input("请输入一个数:"))
b=input("请输入运算符:")
c=float(input("请输入一个数:"))
print(calculate(a,b,c))