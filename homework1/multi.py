# -*- encoding: utf-8 -*-
'''
@File : multi.py
@Time : 2020/03/07 16:14:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#打印输出9*9乘法表，按照下面的格式：
for i in range(1,10):
    for j in range(1,i+1):
         print("""%d*%d=%d""" % (j,i,j*i),end=" ")
    print()
