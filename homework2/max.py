# -*- encoding: utf-8 -*-
'''
@File : max.py
@Time : 2020/03/09 18:47:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#8  请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
# 例如，输入 aaaabbc，输出：a:4



def sort(str_):
    count ={}
    for i in str_:
        count[i]=str_.count(i)
    count1 = {key:value for key,value in count.items() if value == max(count.values())}
    print(count1)

x=input("请输入一个字符串:")
sort(x)