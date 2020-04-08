# -*- encoding: utf-8 -*-
'''
@File : rizhi.py
@Time : 2020/04/07 19:48:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；

def dec(func):
    def wrapper(a,b):
        with open('F:/Python/homework5/jilu.txt',"a+",encoding="utf-8") as f:
            f.write("这里开始执行内部函数%s\n"%(func.__name__))
            result=func(a,b)
            f.write("这里结束执行内部函数%s\n"%(func.__name__))
        
        return result
    return wrapper
@dec
def add(x,y):
    return x+y

print(add(3,5))

