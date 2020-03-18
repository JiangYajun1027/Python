# -*- encoding: utf-8 -*-
'''
@File : b.py
@Time : 2020/03/18 21:40:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#练习2：上一级文件目录中的其他文件夹中打开

with open(r"study\practice\a_file\aa.txt","r",encoding="utf-8")as f:
    print(f.read())