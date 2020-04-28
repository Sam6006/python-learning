# ### 服务器
import socket
#1.创建一个socket对象  默认按照tcp协议创建
sk = socket.socket()
#2.绑定ip 和端口 在网络上注册该主机，让其他主机找到你
'''
bind(元组) 默认本地ip 127.0.0.1 （ip,端口）
'''
sk.bind(("127.0.0.1", 9000))

#3.开启监听
sk.listen()
# listen  accept recv 都是阻塞;如果不满足条件,程序不会往下执行;

# 5.收发数据 quit

while True:
	#4.三次握手
	'''conn 是三次握手的连接对象， addr是对文的ip和端口'''
	conn, addr = sk.accept()
	while True:
		#收消息
		msg = conn.recv(1024)
		print(msg.decode())
		#发送数据
		message = input('老弟，要发什么？>>>>')
		conn.send(message.encode('utf-8'))
		if message == "q":
			break

#四次挥手
conn.close()

#退还端口
sk.close()