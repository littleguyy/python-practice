# -*- coding: cp936 -*-
# python 2.7 

import socket
from scapy.all import *
# IP()、 ICMP()、 TCP()、 UDP()
i=IP()
i.dst="packtpub.samsclass.info"
i.display()
ic=ICMP()
ic.display()
reply=sr1(i/ic)
#send(i/ic)
