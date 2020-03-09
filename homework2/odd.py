# -*- encoding: utf-8 -*-
'''
@File : odd.py
@Time : 2020/03/08 18:04:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#   数字列表请用随机数函数生成;

import random
def odd_(args):
    list_=[]
    for x in args:
        if x%2==1:
            list_.append(x)
    return list_

list1=[random.randint(1,20) for i in range(10)]
print(list1)
print(odd_(list1))
