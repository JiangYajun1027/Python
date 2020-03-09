# -*- encoding: utf-8 -*-
'''
@File : student.py
@Time : 2020/03/09 18:44:42
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
#    A---成绩>=90;  
#    B-->成绩在 [80,90)
#    C-->成绩在 [70,80)
#    D-->成绩<70

import random
def score(x):
    if x>=90:
        return 'A'
    elif x>=80 and x<90:
        return 'B'
    elif x>=70 and x<80:
        return 'C'
    else:
        return 'D'

for i in range(0,20):
    s=random.randint(1,100)
    print("得分:%d,等级:%s"%(s,score(s)))