# -*- encoding: utf-8 -*-
'''
@File : openfile.py
@Time : 2020/03/18 21:14:56
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#练习2：同级目录下的子目录里面打开
import os
print(os.getcwd())
with open(r"study\practice\b_file\a.txt","r",encoding="utf-8")as f:
    print(f.read())