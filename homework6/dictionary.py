# -*- encoding: utf-8 -*-
'''
@File : dictionary.py
@Time : 2020/04/12 19:38:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#三、定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})

class dictclass(object):
    def __init__(self,x):
        self.dic=x
    def del_dict(self,key):
        if key in self.dic.keys():
            del self.dic[key]
            print('删除成功!')
    def get_dict(self,key):
        if key in self.dic.keys():
            return self.dic[key]
        else:
            return 'not found'
    def get_key(self):
        listx=[]
        for k in self.dic.keys():
            listx.append(k)
        return listx
    def update_dict(self,y):
        listy=[]
        dic3=self.dic.copy()
        dic3.update(y)
        for k in dic3:
            listy.append(dic3[k])
        return listy

dic1={'name':'Alice','age':18,'grade':'three'}
dic2={'address':'bejing'}
dictionary=dictclass(dic1)
print(dictionary.get_key())
print(dictionary.get_dict('age'))
dictionary.del_dict('grade')
print(dictionary.update_dict(dic2))


    