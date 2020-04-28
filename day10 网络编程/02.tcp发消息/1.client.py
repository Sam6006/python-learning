# ### client
import socket

#创建tcp对象
sk = socket.socket()

#直接与服务器主机建立连接
'''
connect(元组) （ip, 端口）
'''
sk.connect(("127.0.0.1", 9000))

#send 用来发送消息, recv用来接收消息
sk.send('我爱你，美丽的祖国'.encode('utf-8'))

#接收数据
res = sk.recv(1024)
print(res.decode('utf-8'))


#关闭连接
sk.close()


















