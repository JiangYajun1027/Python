# -*- encoding: utf-8 -*-
'''
@File : print.py
@Time : 2020/03/18 17:12:43
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#练习7:  读取文件里面的内容(包含中文), 进行打印输出显示;
#         注意:  请设置文件的不同编码格式进行观察;  另外,文件内容中包含中文字符;

import sys
print(sys.getfilesystemencoding())
print()

with open('F:/Python/practice/1.txt','r',encoding='utf-8-sig')as f1:
    for line in f1.readlines():
        print(line.strip())
print()

with open('F:/Python/practice/1.txt','r',encoding='utf-8')as f2:
    for line in f2.readlines():
        print(line.strip())
print()

