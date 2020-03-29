# -*- encoding: utf-8 -*-
'''
@File : weekjudge.py
@Time : 2020/03/29 18:29:36
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；

import datetime
x=list(datetime.date(2020,2,17).isocalendar())
#print('{}年第{}周周{}'.format(x[0],x[1],x[2]))


z=list(datetime.date(2020,3,29).isocalendar())
print('{}年第{}周周{}'.format(z[0],z[1]-x[1],z[2]))
