# -*- encoding: utf-8 -*-
'''
@File : smallpro.py
@Time : 2020/03/25 17:28:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#5 文件编程小项目
# (1) 创建一个文件Blowing in the wind.txt
# (2) 在文件头部插入歌名“‘Blowin’ in the wind”
# (3) 在歌名后插入歌手名“Bob Dylan”
# (4) 在文件末尾加上字符串“1962 by Warner Bros. Inc.”
# (5) 在屏幕上打印文件内容


try:
    with open(r'F:/Python/homework3/Blowing in the wind.txt','w')as f1:
        f1.write('How many roads must a man walk down \n')
        f1.write('Before they call him a man \n')
        f1.write('How many seas must a white dove sail \n')
        f1.write('Before she sleeps in the sand \n')
        f1.write('How many times must the cannon balls fly \n')
        f1.write('Before they\'re forever banned \n')
        f1.write('The answer my friend is blowing in the wind \n')
        f1.write('The answer is blowing in the wind\n')
except IOError:
    print("open error")

try:
    with open(r'F:/Python/homework3/Blowing in the wind.txt','r+')as f2:
        txt=f2.readlines()
        txt.insert(0,'‘Blowin’ in the wind\n')
        f2.seek(0,0)
        f2.writelines(txt)
except IOError:
    print("open error")

try:
    with open(r'F:/Python/homework3/Blowing in the wind.txt','r+')as f3:
        txt=f3.readlines()
        txt.insert(1,'Bob Dylan\n')
        f3.seek(0,0)
        f3.writelines(txt)
except IOError:
    print("open error")

try:
    with open(r'F:/Python/homework3/Blowing in the wind.txt','a')as f4:
        f4.write('1962 by Warner Bros. Inc.\n')
except IOError:
    print("open error")

try:
    with open(r'F:/Python/homework3/Blowing in the wind.txt','r') as f5:
        lines =f5.readlines()
        for i in range(0,len(lines)):
            print(lines[i])
except Exception:
    print("open error")

    

