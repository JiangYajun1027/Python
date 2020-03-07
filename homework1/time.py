# -*- encoding: utf-8 -*-
'''
@File : time.py
@Time : 2020/03/07 17:18:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
#提示：可以用字典来统计：key 是单词，value 是单词出现次数；
#先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 
#   如果字典中 key 已经出现了这个单词，那么它对应的 value ，也就是出现次数就 +1； 
#   如果这个单词没出现过，就直接 插入这个单词及 value 为 1 到 字典中；

list=['random','lis','easy','secret','hello','apple','secret','random','easy','hello','secret']
dic={}
for i in list:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
sort_dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
print(sort_dic)  