import socket
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

while 1:
	cmd = input('请输入一个命令>>>')
	sk.send(cmd.encode('utf-8'))

	n = sk.recv(4)
	n = struct.unpack('i', n)[0]
	result = sk.recv(n).decode('gbk')

	print(result)

sk.close()