# -*- encoding: utf-8 -*-
'''
@File : fileshow.py
@Time : 2020/03/29 21:31:53
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
#    名称         日期                   类型（文件夹或者 文件）       大小

import os

head = "{:^50}\t{:^50}\t{:^10}\t{:^10}"
print(head.format("名称", "日期", "类型", "大小",chr(12288)))

def getshow(path):
    they = os.listdir(path)
    for x in they:                                           
        if os.path.isdir(os.path.join(path,x)):
            print(head.format(x, os.path.getmtime(os.path.join(path,x)), 'folder', '', chr(12288)))

        else:
            size = os.path.getsize(os.path.join(path,x))
            print(head.format(x, os.path.getmtime(os.path.join(path,x)), 'file', size, chr(12288)))

if __name__== "__main__":
    getshow('F:/Python')