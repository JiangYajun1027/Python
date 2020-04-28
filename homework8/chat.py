# -*- encoding: utf-8 -*-
'''
@File : chat.py
@Time : 2020/04/25 15:37:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 4 多进程通讯：
#   编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；

import os
import time
import random
from multiprocessing import Process,Queue

def write(queue,m):
    print('Process %s to write:' % os.getpid())
    print('Put %s to queue...' % m)
    queue.put(m)
    time.sleep(random.random())

def read(queue):
    print('Process %s to read:' % os.getpid())
    while True:
        if not queue.empty():
            for i in range(queue.qsize()):
                print(queue.get_nowait())
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    q = Queue()
    while True:
        message = input('请输入消息:')
        pw = Process(target=write, args=(q,message,))
        pw.start()
        pw.join()
        print('是否继续(1是,0否)：')
        flag = int(input())
        if flag == 0:
            break
    pr = Process(target=read, args=(q,))
    pr.start()
    pr.join() 