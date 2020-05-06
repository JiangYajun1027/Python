# -*- encoding: utf-8 -*-
'''
@File : chatclient.py
@Time : 2020/05/05 15:36:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
#客户端

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
host = '127.0.0.1'
port = 8888

while True:
    con=input("我发的消息是:")
    con=con.encode('utf-8')
    client.sendto(con, (host, port))
    msg, addr = client.recvfrom(1024) 
    msg=msg.decode('utf-8')
    print('服务器%s回复的消息是:%s'%(addr,msg))
    #print(client.recv(1024).decode('utf-8'))
    
client.close()
