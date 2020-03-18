# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/03/18 09:15:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#练习3:   一个文件内容的如下,请读取文件的内容, 并输出;
#            姓名      学号      分数
#            张三      101         78
#            李四      102         87
#            王五       103        83

with open('F:/Python/practice/1.txt','r',encoding='utf-8-sig')as f:
    for line in  f.readlines():
        print(line.strip())