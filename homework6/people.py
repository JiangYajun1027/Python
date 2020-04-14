# -*- encoding: utf-8 -*-
'''
@File : people.py
@Time : 2020/04/14 16:54:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import random
class People(object):
    atk=10
    blo=100
    def __init__(self, name,):
        self.name=name
    
    def attack(self, listx,listy):
        if len(listx)==0:
            return 
        if len(listy)==0:
            return 
        x=random.randint(0,len(listx)-1)
        y=random.randint(0,len(listy)-1)
        if listx[x].blo>0 and listy[y].blo>0:
            print('%s攻击%s\n'%(listx[x].name,listy[y].name))
            print('%s的攻击力降低2,%s的血量减少10\n'%(listx[x].name,listy[y].name))
            listy[y].blo=listy[y].blo-10
            listx[x].atk=listx[x].atk-2
            if listy[y].blo<=0:
                print('%s血量已空，阵亡\n'%(listy[y].name))
                listy.remove(listy[y])
        else:
            print('攻击无效\n')
        