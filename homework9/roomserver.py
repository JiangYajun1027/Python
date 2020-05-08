# -*- encoding: utf-8 -*-
'''
@File : chatroom.py
@Time : 2020/05/05 14:01:18
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#4 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；
#服务器

import socket
import os
import threading

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    
    address = (('127.0.0.1',8080))
    server.bind(address)
    #server.listen(5)
    
    userdic={}

    t1 = threading.Thread(target=recvmsg,args=(server,userdic,))

    t1.start()

def recvmsg(server,userdic):
    while True:
        msg,addr = server.recvfrom(1024)
        msg=msg.decode()
        print(msg)

        msglist = msg.split(' ')
        if msglist[0] == 'login':
            userdic[msglist[1]]=addr
            print('%s进入聊天室'%msglist[1])

        elif msglist[0] == 'quit':
            message = '%s退出了聊天室' % msglist[1]
            for u in userdic:
                if u!=msglist[1]:
                    server.sendto(message.encode(),userdic[u])
                else:
                    server.sendto('exit'.encode(),userdic[msglist[1]])
            del userdic[msglist[1]]

        else:
            #msgdic:['name','speak','content']
            content = ' '.join(msglist[2:])          #获取完整发送内容
            message = '%s ：%s' % (msglist[0],content)
            for u in userdic:
                if u!= msglist[0]:
                    server.sendto(message.encode(),userdic[u])

    server.close()
    os._exit(0)
        

# def sendmsg(server,userdic):
#     while True:
#         msg = input('服务器输入消息:')
#         if msg == "exit":
#             print("服务器退出了聊天室")
#             server.close()
#             break
#         for u in userdic:
#             server.sendto(msg.encode('utf-8'),userdic[u])
#     os._exit(0)
    

if __name__ == '__main__':
    main()
