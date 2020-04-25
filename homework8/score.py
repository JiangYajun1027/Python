# -*- encoding: utf-8 -*-
'''
@File : score.py
@Time : 2020/04/24 19:26:56
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 1  有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#      B 利用线程池来实现；

import os
import time
import random
import threading
from multiprocessing import Pool

def Astudent(s1):
    start = time.time()
    print("%s开始执行,进程号为%d\n" % (s1,os.getpid()))
    ita=iter(s1)
    for x in ita:
        print(x, end=" ")
    print('\n')
    time.sleep(random.random()*2) 
    stop = time.time()
    print(s1,"执行完毕，耗时%0.2f\n" % (stop-start))

def Bstudent(s2):
    start = time.time()
    print("%s开始执行,进程号为%d\n" % (s2,os.getpid()))
    itb=iter(s2)
    for y in itb:
        print(y, end=" ")
    print('\n')
    time.sleep(random.random()*2) 
    stop = time.time()
    print(s2,"执行完毕，耗时%0.2f\n" % (stop-start))
    

if __name__=='__main__':
    stu=[]
    while len(stu)<100:
        stu.append(random.randint(0,100))
    print(stu)
    print('\n')

    list1=stu[0:20]
    list2=stu[20:40]
    list3=stu[40:60]
    list4=stu[60:80]
    list5=stu[80:100]

    print("------------------------------------------start------------------------------------------")
    t1 = threading.Thread(target=Astudent(list1))
    t2 = threading.Thread(target=Astudent(list2))
    t3 = threading.Thread(target=Astudent(list3))
    t4 = threading.Thread(target=Astudent(list4))
    t5 = threading.Thread(target=Astudent(list5))
    print("------------------------------------------end------------------------------------------")

    student=[list1,list2,list3,list4,list5]
    po = Pool(3)  
    for i in student:
        po.apply_async(Bstudent,(i,))

    print("------------------------------------------start------------------------------------------")
    po.close()  
    po.join() 
    print("------------------------------------------end------------------------------------------")
