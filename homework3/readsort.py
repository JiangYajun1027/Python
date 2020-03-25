# -*- encoding: utf-8 -*-
'''
@File : readsort.py
@Time : 2020/03/24 20:16:06
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出

stulist=[]
try:
    with open('F:/Python/homework3/student.txt','r',encoding='utf-8-sig')as f:
        for line in  f.readlines():
            line = line.strip("\n")  
            s = line.split(" ")  
            stulist.append(s)
        print(stulist)
except Exception:
    pass

try:
    x=stulist[0]
    del stulist[0]
    stulist.sort(key=lambda x:int(x[2]))
    stulist.reverse() 
    stulist.insert(0,x)
    for line in stulist:
        y=" ".join(line)
        print(y)
except Exception:
    pass