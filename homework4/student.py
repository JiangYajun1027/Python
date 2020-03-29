# -*- encoding: utf-8 -*-
'''
@File : student.py
@Time : 2020/03/29 19:25:50
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
        # Tom   admin   XXXXX
        # Jack   root      XXXXX   

import hashlib

dic1={
    'name':'Alice',
    'account':'111',
    'password':'111',
}
dic2={
    'name':'Tom',
    'account':'112',
    'password':'112',
}
dic3={
    'name':'Jack',
    'account':'113',
    'password':'113',
}
dic4={
    'name':'Bob',
    'account':'114',
    'password':'114',
}
dic5={
    'name':'Cindy',
    'account':'115',
    'password':'115',
}
with open('F:/Python/homework4/student.txt',"w",encoding="utf-8")as f:
    listx=[dic1,dic2,dic3,dic4,dic5]
    for x in listx:
        h = hashlib.sha256()
        h.update(bytes(x['password'], encoding='utf-8'))
        x['password'] = h.hexdigest()
        f.write(x['name']+'   '+x['account']+'   '+x['password']+'\n')