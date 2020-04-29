import socket
import struct
import time
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

time.sleep(0.1)

#先接收要截取的长度是多少
n = sk.recv(4)
n = struct.unpack('i', n)[0]

print(n)
#再去接收真实的数据，防止粘包
print(sk.recv(n))
print(sk.recv(10))

sk.close()