# -*- encoding: utf-8 -*-
'''
@File : number.py
@Time : 2020/03/06 17:06:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#1 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；

a=[x for x in range(0,51)]
print("列表元素为:",a)

odd=filter(lambda x:x%2==1,a)
print("奇数有:",list(odd))

even=filter(lambda x:x%2==0,a)
print("偶数有:",list(even))

b=[]
for num in a:
    if num >1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            b.append(num)
print("质数有:",b)

li=filter(lambda x:x%2==0 and x%3==0,a)
print("能同时被2和3整除的数有:",list(li))
