import socket
import os
import sys

# 第三方库
from 网络 import 创建网络

if __name__ == '__main__':
    创建网络.本地服务器地址='127.0.0.1'
    创建网络.本地服务器端口=1082
    插座= 创建网络.申请插座()
    print("服务器的socket建立了")
    插座.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    创建网络.绑定插座(插座)
    print('服务器的socket绑定到%s:%d'%(创建网络.本地服务器地址,创建网络.本地服务器端口))
    创建网络.监听插座(插座,500)
    print('服务器开始监听端口%d，等待连接。'%创建网络.本地服务器端口)    
    while True:
        连线,客户端地址 = 创建网络.插座接受的连接(插座)
        print("服务器sock连接到客户端地址：",客户端地址)
        try:
            创建网络.连线超时(连线, 5)
            接收缓冲区=创建网络.连线接收的内容(连线, 2048)
            print('客户端发来数据：%s'%接收缓冲区)
            # if headers["Method"]=="CONNECT":
            发送的内容=b'HTTP/1.1 200 Connection Established\r\n\r\n'
            创建网络.连线发送(连线, 发送的内容)
            print("向客户端发送了HTTP/1.1 200 Connection Established\r\n\r\n")
            接收缓冲区=创建网络.连线接收的内容(连线, 2048)
            print('客户端再次发来数据：%s'%接收缓冲区)
            #else:  
                #print("error") 
        except socket.timeout:  
            print ('time out')
        创建网络.关闭连接(连线)
    创建网络.关闭插座(插座)
