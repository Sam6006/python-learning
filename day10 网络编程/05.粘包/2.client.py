import socket
import time
'''
#解决黏包场景:
	应用场景在实时通讯时,需要阅读此次发的消息是什么
#不需要解决黏包场景:
	下载或者上传文件的时候,最后要把包都结合在一起,黏包无所谓.
'''

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

time.sleep(0.1)


#收发数据逻辑

n = int(sk.recv(1).decode('utf-8'))
print(n, type(n))
print(sk.recv(n))
print(sk.recv(10))

sk.close()