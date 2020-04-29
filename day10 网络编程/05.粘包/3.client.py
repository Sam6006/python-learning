import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
time.sleep(0.1)

#收发数据逻辑
n = int(sk.recv(8))
print(n,type(n))

print(sk.recv(n))
print(sk.recv(10))


sk.close()