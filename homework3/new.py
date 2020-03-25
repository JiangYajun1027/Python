# -*- encoding: utf-8 -*-
'''
@File : new,.py
@Time : 2020/03/24 20:25:06
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#4 题目要求：
#在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
#将当前img目录所有以.png结尾的后缀名改为.jpg.

import os
path=os.path.abspath('.')
os.mkdir("img")
path=os.path.join(path,'img')
print(path)
name=['aa.png','bb.png','cc.png','ab.png','ac.png','ba.png','bc.png','ca.png','cb.png','dd.png']
try:
    for i in range(0,10):
        with open(os.path.join(path,name[i]),'w',encoding='utf-8')as f:
            continue
except Exception:
    print("open error")

def change(pathname,before,after):
    try:
        if os.path.exists(pathname):
            files=[filename for filename in os.listdir(pathname) if filename.endswith(".png")]
            list1=[os.path.splitext(filename)[0] for filename in files]
            list2=[]
            for x in list1:
                old=os.path.join(pathname,x+before)
                new=os.path.join(pathname,x+after)
                os.rename(old,new)
                list2.append(new)
    except Exception:
        print("重命名失败")
    else:
        print("重命名成功")

change(path,'.png','.jpg')

