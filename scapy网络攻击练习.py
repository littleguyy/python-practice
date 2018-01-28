# python 3.6.3 网络攻击 scapy 练习

import socket
from scapy.all import *
# 用scapy模块，建立网络对象：
# IP()、 ICMP()、 TCP()、 UDP()

def test_连接socket():
    s=socket.socket()
    s.settimeout(2)

    port=input("端口号：")
    try:
        s.connect(("packtpub.samsclass.info",int(port))) # packtpub.samsclass.info
        print(s.recv(1024))
        s.close()
    except socket.error as err:
        print(err)
        s.close()

def scapy攻击测试():
    
    i=IP()
    i.dst="192.168.1.1"
    i.display()
    
    ic=ICMP()
    ic.display()

    reply=sr1(i/ic)

    
def http头攻击():
    s=socket.socket()
    s.settimeout(2)

    target=b'packtpub.samsclass.info'
    s.connect((target,80))

    请求=b'HEAD / HTTP/1.1\r\nHost: '+target+b'\r\n\r\n'

    print("发送请求： %s"%str(请求))
    s.send(请求)

    print("接收服务器应答： ")
    print(s.recv(1024))

    s.close()

def httpGET攻击():
    s=socket.socket()
    s.settimeout(2)

    目标=b'www.baidu.com'
    s.connect((目标,80))

    请求=b'GET / HTTP/1.1\r\nHost: '+目标+b'\r\n\r\n'
    print("发送请求：\n %s"%请求)
    s.send(请求)

    print("接收服务器应答：\n %s"%s.recv(1024))
    s.close()
    
if __name__=="__main__":
    # test_连接socket()
    # http头攻击()
    # httpGET攻击()
    scapy攻击测试()
