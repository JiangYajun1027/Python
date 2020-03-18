# -*- encoding: utf-8 -*-
'''
@File : path.py
@Time : 2020/03/18 15:39:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#练习1:  在window平台下练习os.path 相关方法的使用

import os
pwd = os.path.abspath('.')
print(pwd)
print("当前工作路径为:",os.getcwd())
print( os.path.basename('D:\\CodeProjects\\PythonProjects\\opms\\study\\practice\\path.py') )   # 返回文件名
print( os.path.dirname('D:\\CodeProjects\\PythonProjects\\opms\\study\\practice\\path.py') )    # 返回目录路径
print( os.path.split('D:\\CodeProjects\\PythonProjects\\opms\\study\\practice\\path.py') )      # 分割文件名与路径
print( os.path.join('study','practice','path.py') )  # 将目录和文件名合成一个路径
