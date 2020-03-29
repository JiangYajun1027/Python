# -*- encoding: utf-8 -*-
'''
@File : copytxt.py
@Time : 2020/03/29 20:05:49
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#5  通过Python来模拟实现一个txt文件的拷贝过程;

with open('F:/Python/homework4/1.txt',"r",encoding="utf-8") as f1:
    with open('F:/Python/homework4/2.txt',"w",encoding="utf-8") as f2:
        for line in f1.readlines():
            f2.write(line)