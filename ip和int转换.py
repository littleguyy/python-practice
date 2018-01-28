import socket,struct
packedIP=socket.inet_aton('60.27.172.87')
print('%s'%struct.unpack("!L",packedIP)[0])
print('%s'%socket.inet_ntoa(struct.pack('!L',1008446551)))
