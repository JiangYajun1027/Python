# -*- encoding: utf-8 -*-
'''
@File : series.py
@Time : 2020/03/07 16:11:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#前面2个元素为0，1，输出100以内的斐波那契数列；

f1 = 0
f2 = 1
print(f1)
print(f2)
for n in range(3,101):
    fn = f2 + f1
    if fn<=100:
        print(fn)
        f1,f2 = f2,fn