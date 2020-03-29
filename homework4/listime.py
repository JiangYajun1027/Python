# -*- encoding: utf-8 -*-
'''
@File : listime.py
@Time : 2020/03/29 17:01:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）

import datetime
from collections import deque

listx=['sd',14,'stbrt',907,235,(1,2,3),[99,88],{'k':'v'},'erv53',691]
start1 = datetime.datetime.now()
print(start1)
listx.insert(0,555)
listx.append('555')
end1 = datetime.datetime.now()
print(end1)
time1=(end1 - start1).seconds
print(time1)

print('*************************************************')

start2 = datetime.datetime.now()
print(start2)
q=deque(listx)
q.appendleft(555)
q.appendleft('555')
end2 = datetime.datetime.now()
print(end2)
time2=(end2 - start2).seconds
print(time2)

print('差值为：{}'.format(time2-time2))