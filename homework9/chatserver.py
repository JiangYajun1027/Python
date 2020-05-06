# -*- encoding: utf-8 -*-
'''
@File : chat.py
@Time : 2020/05/05 14:00:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
#服务器

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
host = '127.0.0.1'
port = 8888
server.bind((host, port))

while True:

    data, addr = server.recvfrom(1024)
    data=data.decode('utf-8')
    print('客户端%s发的消息是:%s'%(addr,data))
    con=input("我回复的消息是:")
    con=con.encode('utf-8')
    server.sendto(con, addr)

server.close()