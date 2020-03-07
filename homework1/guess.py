# -*
# - encoding: utf-8 -*-
'''
@File : guess.py
@Time : 2020/03/07 16:54:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；

secret=5
guess = -1
N = 0
while guess != secret:
    guess = int(input('请输入0--10之间的整数：\n'))
    N+=1
    if guess > secret:
        print('猜测过大！\n')
    if guess < secret:
        print('猜测过小！\n')
    if(N>=10):
        print('次数用完，退出程序')
        break
if guess == secret:
    print('猜中了！')