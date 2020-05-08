# -*- encoding: utf-8 -*-
'''
@File : roomclient.py
@Time : 2020/05/07 20:17:49
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#4 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；
#客户端

import socket
import os
import sys
import threading

def main():

    address = ('127.0.0.1',8080)

    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    name = input('请输入姓名：')       
    message = 'login ' + name
    client.sendto(message.encode('utf-8'),address)          # 2.把姓名包装，发送给服务端
    print('%s成功进入聊天室'%name)
    
    t1 = threading.Thread(target=sendmsg,args=(client,name,address,))
    t2 = threading.Thread(target=recvmsg,args=(client,))
    
    t1.start()
    t2.start()

def sendmsg(client,name,address):
    while True:
        content=input('请发言（输入quit退出）：')
        if content == 'quit':
            message =  'quit ' + name
            client.sendto(message.encode(),address)
            
        message = '%s speak %s' % (name,content)
        client.sendto(message.encode('utf-8'),address)
        
    client.close()
    os._exit(0)
    

def recvmsg(client):
    while True:
        data,addr = client.recvfrom(1024)
        if data.decode() == 'exit':
            client.close()
            os._exit(0) #os._exit(n), 直接退出, 不抛异常, 不执行相关清理工作. 常用在子进程的退出.
        print(data.decode('utf-8')+'\n请发言（输入quit退出）：',end='')

if __name__ == "__main__":
    main()
