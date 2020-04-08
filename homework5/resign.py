# -*- encoding: utf-8 -*-
'''
@File : resign.py
@Time : 2020/04/08 19:42:38
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）

def dec(func):
    def wrapper():
        print("请输入账号:")
        account=input()
        print("请输入密码:")
        password=input()
        if account=='张三' and password=='123456':
            func()
        else:
            print('无法认证，无法调用函数')
    return wrapper
@dec
def hanshu():
    print('函数') 

hanshu()