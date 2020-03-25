# -*- encoding: utf-8 -*-
'''
@File : compare.py
@Time : 2020/03/25 19:48:37
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#6  在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
#    比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);

import re
try:
    with open('F:/Python/homework3/1.txt',"r")as f1:
        words=f1.read()
        words=re.sub(',.\'()\"',' ',words)
        listx=words.replace('\n',' ').replace('  ',' ').lower().split(' ')
        dic={}
        for word in listx:
            if word in dic.keys():
                dic[word]+=1
            else:
                dic[word]=1
        dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        with open('F:/Python/homework3/count1.txt',"w")as f2:
            for x in dic:
                f2.write("%s\t%s\n"%(x[0],x[1]))
except Exception as error1:
    print(error1)

try:
    with open('F:/Python/homework3/2.txt',"r")as f3:
        words=f3.read()
        words=re.sub(',.\'()\"',' ',words)
        listx=words.replace('\n',' ').replace('  ',' ').lower().split(' ')
        dic={}
        for word in listx:
            if word in dic.keys():
                dic[word]+=1
            else:
                dic[word]=1
        dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        with open('F:/Python/homework3/count2.txt',"w")as f4:
            for x in dic:
                f4.write("%s\t%s\n"%(x[0],x[1]))
except Exception as error2:
    print(error2)

count=0
counts=0
list1=[]
list2=[]
try:
    with open('F:/Python/homework3/count1.txt',"r") as f5:
        for word in f5.readlines():
            wordsplit=word.split("\t")
            list1.append(wordsplit[0])
            count+=1
            if count==10:
                break
except Exception as error3:
    print(error3)
print(list1)
try:
    with open('F:/Python/homework3/count2.txt',"r") as f6:
        for word in f6.readlines():
            wordsplit=word.split("\t")
            list2.append(wordsplit[0])
            counts+=1
            if counts==10:
                break
except Exception as error4:
    print(error4)
print(list2)
num=0
for x in list1:
    for y in list2:
        if x==y:
            num+=1
print('文章相似度为:{}%'.format(num*10))

