# ### socketserver 实现tcp连接的并发操作

import socketserver

'''
#网络协议的最底层就是socket,基于原有socket模块,又封装了一层,就是socketserver
socketserver 为了实现tcp协议,server端的并发.
'''


class MyServer(socketserver.BaseRequestHandler):
	def handle(self):
		# print(self.request) # conn = "<socket.socket fd=456, family=AddressFamily.AF_INET,
		# type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9000), raddr=('127.0.0.1', 63623)>"
		# self.request 相当于conn ,在socketserver底层已经给你封装好了,直接拿来用就可以;
		conn = self.request
		# ('127.0.0.1', 63692) request和client_address  就是sk.accept() 三次握手的返回值,只不过用两个不同的变量接受了.
		# print(self.client_address)
		'''
		while True:
			msg = conn.recv(1024).decode("utf-8")
			print(msg)
			conn.send(msg.upper().encode("utf-8"))
		'''

# 创建一个对象 , 通过 ThreadingTCPServer创建 ThreadingTCPServer( ip端口 , 自定义类 )
server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), MyServer)

# 循环调用
server.serve_forever()
