# -*- encoding: utf-8 -*-
'''
@File : wsort.py
@Time : 2020/03/18 15:48:21
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#练习4:
#   一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
#            姓名      学号      分数
#            张三      101        78
#            李四      102        87
#            王五      103        83

stulist=[]
with open('F:/Python/practice/1.txt','r',encoding='utf-8-sig')as f:
    for line in  f.readlines():
        line = line.strip("\n")  
        s = line.split("      ")  
        stulist.append(s)
x=stulist[0]
del stulist[0]
stulist.sort(key=lambda x:int(x[2]))
stulist.reverse() 
print(stulist)
stulist.insert(0,x)
print(stulist)

with open('F:/Python/practice/2.txt','w',encoding='utf-8-sig')as fl:
    for line in stulist:
        y=" ".join(line)
        fl.write(y+'\n')



