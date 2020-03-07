# -*- encoding: utf-8 -*-
'''
@File : struct.py
@Time : 2020/03/07 16:22:31
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  将这10个员工，按照工资从高到低打印输出；
#提示：可以组合使用我们的序列数据类型；
dic0={
    'number':110,
    'name':'Alice',
    'year':10,
    'money':3900
}
dic1={
    'number':111,
    'name':'Alice',
    'year':5,
    'money':2700
}
dic2={
    'number':112,
    'name':'Alice',
    'year':8,
    'money':3200
}
dic3={
    'number':113,
    'name':'Alice',
    'year':1,
    'money':2300
}
dic4={
    'number':114,
    'name':'Alice',
    'year':4,
    'money':3000
}
dic5={
    'number':115,
    'name':'Alice',
    'year':20,
    'money':4600
}
dic6={
    'number':116,
    'name':'Alice',
    'year':13,
    'money':3800
}
dic7={
    'number':117,
    'name':'Alice',
    'year':25,
    'money':4700
}
dic8={
    'number':118,
    'name':'Alice',
    'year':16,
    'money':4100
}
dic9={
    'number':119,
    'name':'Alice',
    'year':2,
    'money':2800
}
list=[dic0,dic1,dic2,dic3,dic4,dic5,dic6,dic7,dic8,dic9]
list.sort(key=lambda k:(k.get('money',0)),reverse=True)
for x,r in enumerate(list):
    print('x[%d]\t money:%d\t number:%d\t name:%s\t year:%d\t' %(x,r['money'],r['number'],r['name'],r['year']))
    