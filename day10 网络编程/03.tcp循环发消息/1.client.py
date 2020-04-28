# ### client
import socket

#创建tcp对象
sk = socket.socket()

#直接与服务器主机建立连接
'''
connect(元组) （ip, 端口）
'''
sk.connect(("127.0.0.1", 9000))

while True:
	#发息消
	message = input('>>>>>>>')
	sk.send(message.encode('utf-8'))
	#收消息
	res = sk.recv(1024)
	if res == b'q':
		break
	print(res.decode())
#关闭连接
sk.close()


















