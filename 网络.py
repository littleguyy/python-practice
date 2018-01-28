import socket
import os
import sys

class 网络:
    def __init__(self):
        self.本地服务器地址='127.0.0.1'
        self.本地服务器端口=1081
        self.远端服务器地址='0.0.0.0' # 填写自己的服务器地址（域名或IP都可以）
        self.远端服务器开放端口=5000 #填写自己的服务器开放端口
        
    def 申请插座(self):
        插座=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return 插座
    
    def 绑定插座(self, 插座):
        插座.bind((self.本地服务器地址, self.本地服务器端口))
        
    def 自定义绑定插座(self, 插座, 本地服务器地址, 本地服务器端口):
        插座.bind((本地服务器地址, 本地服务器端口))

    def 监听插座(self, 插座, 连接数):
        插座.listen(连接数)

    def 插座接受的连接(self, 插座):
        return 插座.accept()

    def 连线超时(self, 连线, 时间):
        连线.settimeout(时间)

    def 连线接收的内容(self, 连线, 缓冲区大小):
        return 连线.recv(缓冲区大小)

    def 连线发送(self, 连接, 发送内容):
        连接.send(发送内容)

    def 关闭连接(self, 连接):
        连接.close()

    def 关闭插座(self, 插座):
        插座.close()
        
创建网络=网络()
