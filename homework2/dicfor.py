# -*- encoding: utf-8 -*-
'''
@File : dicfor.py
@Time : 2020/03/08 18:42:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#5  写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;{'name':'jiangyajun','age':'18','class':'1801'}
 
def lengthfor(dic):
    for k,v in dic.items():
        if len(v)>2:
            dic[k]=v[0:2]
    return dic

dic_=eval(input("请输入字典元素:"))
print("改写后的字典为:")
print(lengthfor(dic_))
