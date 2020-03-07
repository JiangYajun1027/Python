# -*- encoding: utf-8 -*-
'''
@File : random.py
@Time : 2020/03/07 15:52:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#使用random模块，生成随机数，来初始化一个列表，元组；
#使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；

import random
list1=[random.randint(1,10) for i in range(10)]
tuple1=(random.randint(1,10),random.randint(11,20))
print(list1)
print(tuple1)