# -*- encoding: utf-8 -*-
'''
@File : judge.py
@Time : 2020/03/08 18:25:19
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#1 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
def judge(a):
    return len(a)

b=eval(input("请输入对象:"))
print("""长度为:%d"""%judge(b))