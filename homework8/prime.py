# -*- encoding: utf-8 -*-
'''
@File : prime.py
@Time : 2020/04/25 10:40:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 3  多进程练习：
# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度。

import time
from multiprocessing import Process

def judgecommon(lista):
    listb=[]
    start=time.time()
    for num in lista:
        if num==1:
            continue
        if num==2:
            listb.append(num)
        else:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                listb.append(num)
                    
    stop=time.time()
    print("不使用多进程:执行完毕，耗时%0.2f\n" % (stop-start))
    print("不使用多进程:个数为:%d"%(len(listb)))

def judgeprocess(lista,x):
    count=0
    for num in lista:
        if num==1:
            continue
        if num==2:
            count=count+1
        else:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                count=count+1
    print("使用%d个进程:个数为:%d"%(x,count))

def use(lista,n):
    start=time.time()
    for x in lista:
        p = Process(target=judgeprocess,args=(x,n,))
        p.start()
        #p.join()
    stop=time.time()
    print("使用%d进程:执行完毕，耗时%0.2f\n" % (n,(stop-start)))

if __name__=='__main__':
    a=[x for x in range(1,100001)]
    list1=a[0:20000]
    list2=a[20000:40000]
    list3=a[40000:60000]
    list4=a[60000:80000]
    list5=a[80000:100000]
    listx=[list1,list2,list3,list4,list5]

    list11=a[0:25000]
    list22=a[25000:50000]
    list33=a[50000:75000]
    list44=a[75000:100000]
    listy=[list11,list22,list33,list44]

    list111=a[0:10000]
    list222=a[10000:20000]
    list333=a[20000:30000]
    list444=a[30000:40000]
    list555=a[40000:50000]
    list666=a[50000:60000]
    list777=a[60000:70000]
    list888=a[70000:80000]
    list999=a[80000:90000]
    list000=a[90000:100000]
    listz=[list111,list222,list333,list444,list555,list666,list777,list888,list999,list000]

    judgecommon(a)
    print('------------------------------------------5个进程------------------------------------------')
    use(listx,5)
    print('------------------------------------------4个进程------------------------------------------')
    use(listy,4)
    print('------------------------------------------10个进程------------------------------------------')
    use(listz,10)

