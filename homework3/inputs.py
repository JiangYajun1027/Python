# -*- encoding: utf-8 -*-
'''
@File : inputs.py
@Time : 2020/03/24 19:21:18
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；


try:
    lines=[]
    print("请输入任意行文字信息：")
    while True:
        line = input().strip()
        if line == '':
            break
        line = list(line.split())
        lines.append(line)
except Exception:
    pass

try:
    with open('F:/Python/homework3/input.txt',"w",encoding="utf-8")as f:
        for line in lines:
            x=" ".join(line)
            f.write(x+'\n')
except IOError:
    print('cannot open')


