# -*- encoding: utf-8 -*-
'''
@File : pick.py
@Time : 2020/03/18 20:24:42
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#练习6:
#  给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去;

import pickle
data1={
   '学号':101,
   '姓名':'Amy',
   '年龄':18
}
data2={
   '学号':102,
   '姓名':'Bob',
   '年龄':22
}
data3={
   '学号':103,
   '姓名':'Cindy',
   '年龄':16
}
data4={
   '学号':104,
   '姓名':'David',
   '年龄':24
}
data5={
   '学号':105,
   '姓名':'Elic',
   '年龄':20
}
listx=[data1,data2,data3,data4,data5]
f = open("F:/Python/practice/3.txt", "wb")
pickle.dump(listx, f)
f.close()
