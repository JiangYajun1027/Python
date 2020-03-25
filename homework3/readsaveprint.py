# -*- encoding: utf-8 -*-
'''
@File : readsaveprint.py
@Time : 2020/03/24 19:59:56
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx

listx=[]
try:
    with open('F:/Python/homework3/input.txt','r',encoding='utf-8-sig')as f:
        for line in  f.readlines():
            line = line.strip("\n")    
            listx.append(line)
except IOError:
    print('cannot open')

x=len(listx)
for i in range(0,x):
    print('#第{}行:{}'.format(i+1,listx[i]))
    