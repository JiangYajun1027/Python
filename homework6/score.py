# -*- encoding: utf-8 -*-
'''
@File : score.py
@Time : 2020/04/12 19:38:46
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#      封装方法，求单个学生的总分，平均分，以及打印学生的信息。

class Student(object):
    def __init__(self,name,age,sex,English,Math,Chinese):
        self.name = name
        self.age = age
        self.sex = sex
        self.English = English
        self.Math = Math
        self.Chinese = Chinese
    def sum(self):
        sumscore = self.English + self.Math + self.Chinese
        return sumscore

    def avg(self):
        avgscore = (self.English + self.Math + self.Chinese) / 3
        return avgscore

    def info(self):
        print('名字:%s\n年龄:%d\n性别:%s\n'%(self.name,self.age,self.sex))

s1=Student('Alice',18,'female',78,95,86)
print('总分:%d'%s1.sum())
print('平均分:%.2f'%s1.avg())
s1.info()