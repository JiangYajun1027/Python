# -*- encoding: utf-8 -*-
'''
@File : filesize.py
@Time : 2020/03/29 21:32:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#7 使用python代码统计一个文件夹中所有文件的总大小

import os

def getsize(path):
    size = 0
    they = os.listdir(path)
    for x in they:                                           
        if os.path.isdir(os.path.join(path,x)):
            size=  size + getsize(os.path.join(path,x))
        else:
            size = size + os.path.getsize(os.path.join(path,x))
    return size

a = getsize('F:/Python/')
print('大小为: %.2f Mb'%(a/1024/1024))