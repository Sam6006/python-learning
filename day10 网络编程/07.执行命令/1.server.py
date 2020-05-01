import socket
import subprocess
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

conn, addr = sk.accept()

while 1:
	cmd = conn.recv(1024).decode('utf-8')
	r = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	#保存正确结果的一个管道
	stdout = r.stdout.read()
	n1 = struct.pack('i', len(stdout))

	#保存错误结果的一个管道
	stderr = r.stderr.read()
	n2 = struct.pack('i', len(stderr))

	if stderr:
		conn.send(n2)
		conn.send(stderr)
	else:
		conn.send(n1)
		conn.send(stdout)
'''
# subprocess.Popen(cmd,shell=True,subprocess.stdout,subprocess.stderr)
# cmd : 代表系统命令
# shell = True   代表这条命令是 系统命令,告诉操作系统,将cmd当成系统命令去执行
# stdout   是执行完系统命令之后,用于保存正确结果的一个管道
# stderr   是执行完系统命令之后,用于保存错误结果的一个管道

'''
conn.close()
sk.close()
