# -*- encoding: utf-8 -*-
'''
@File : three.py
@Time : 2020/04/08 19:50:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#4  编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#      三个目标函数分别为：
#      A 打印输出20000之内的素数；
#      B 计算整数2-10000之间的素数的个数；
#      C 计算整数2-M之间的素数的个数；
#   可以观看给的视频材料，仿照示例来做；

def Aouter(func):
    def Ainner():
        func()
    return Ainner

@Aouter
def Amethod():
    num=[]
    for i in range(2,20000):
        for j in range(2,i):
            if(i%j==0):
                break
            else:
                num.append(i)
                break
    print(num)

Amethod()


def Bouter(func):
    def Binner():
        result=func()
        return result
    return Binner

@Bouter
def Bmethod():
    count=0
    for i in range(2,10000):
        for j in range(2,i):
            if(i%j==0):
                break
            else:
                count+=1
    return count

print(Bmethod())


def Couter(func):
    def Cinner(M):
        result=func(M)
        return result
    return Cinner

@Couter
def Cmethod(M):
    count=0
    for i in range(2,M):
        for j in range(2,i):
            if(i%j==0):
                break
            else:
                count+=1
    return count

print(Cmethod(100))