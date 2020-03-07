# -*- encoding: utf-8 -*-
'''
@File : dic.py
@Time : 2020/03/06 17:36:49
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#一个字典中，存放了10个学生的学号（key）和分数（value）；请筛选输出，大于80分的同学（按照格式：学号：分数）；

data={
    110:78,
    111:36,
    112:95,
    113:66,
    114:71,
    115:82,
    116:97,
    117:42,
    118:59,
    119:44
}
print("大于80分的同学有:")
for k,v in data.items():
    if(v>80):
        print(k,':',v)