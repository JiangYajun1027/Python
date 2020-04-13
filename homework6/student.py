# -*- encoding: utf-8 -*-
'''
@File : student.py
@Time : 2020/04/12 19:37:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#二 定义一个学生Student类。有下面的类属性：
# 1 姓名 name
# 2 年龄 age
# 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:

class Student():
    name=''
    age=0
    Chinese=0
    Math=0
    Engliash=0
    def __init__(self,a,b,c,d,e):
        self.name=a
        self.age=b
        self.Chinese=c
        self.Math=d
        self.Engliash=e
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_score(self):
        if self.Chinese>=self.Math:
            if self.Engliash>=self.Chinese:
                return self.Engliash
            else:
                return self.Chinese
        else:
            if self.Engliash>=self.Math:
                return self.Engliash
            else:
                return self.Math

s1=Student('Alice',18,98,100,85)
print(s1.get_name())
print(s1.get_age())
print(s1.get_score())