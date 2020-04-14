# -*- encoding: utf-8 -*-
'''
@File : dog.py
@Time : 2020/04/14 16:54:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import random
class Dog(object):
    atk=15
    blo=80
    def __init__(self, name):
        self.name=name
    
    def attack(self, listy,listx):
        if len(listy)==0:
            return 
        if len(listx)==0:
            return 
        y=random.randint(0,len(listy)-1)
        x=random.randint(0,len(listx)-1)
        if listy[y].blo>0 and listx[x].blo>0:
            print('%s攻击%s\n'%(listy[y].name,listx[x].name))
            print('%s的攻击力降低3,%s的血量减少10\n'%(listy[y].name,listx[x].name))
            listx[x].blo=listx[x].blo-10
            listy[y].atk=listy[y].atk-3
            if listx[x].blo<=0:
                print('%s血量已空，阵亡\n'%listx[x].name)
                listx.remove(listx[x])
        else:
            print('攻击无效\n')