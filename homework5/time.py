# -*- encoding: utf-8 -*-
'''
@File : time.py
@Time : 2020/04/07 19:26:09
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#1  编写一个装饰器，能计算其他函数的运行时间；

import time,random
def outer(func):
    def inner():
        t1=time.time()
        func()
        t2=time.time()
        print("运行时间为:%s"%(t2-t1))
    return inner

@outer
def yunxing():
    time.sleep(random.randrange(1,5))
    print("运行中")

yunxing()