# -*- encoding: utf-8 -*-
'''
@File : resign.py
@Time : 2020/03/29 19:49:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#4  (继续上面的练习) 模拟用户登录:
#    5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);

import hashlib
print('请输入姓名:')
x=input()
with open('F:/Python/homework4/student.txt',"r",encoding="utf-8") as f:
    for line in f.readlines():
        stu=line.split()
        if x==stu[0]:
            print('请输入账号:')
            y=input()
            if y==stu[1]:
                print('请输入密码:')
                z=input()
                h = hashlib.sha256()
                h.update(bytes(z, encoding='utf-8'))
                z= h.hexdigest()
                if z==stu[2]:
                    print('登录成功')
                    break
                else:
                    print('密码错误')
                    break
            else:
                print('账号错误')
                break
        else:
            print('该同学不存在')
            break        