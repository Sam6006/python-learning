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

#4.三次握手
'''
conn 是三次握手的连接对象， addr是对文的ip和端口
'''
conn, addr = sk.accept()
print(conn)
# <socket.socket fd=476, family=AddressFamily.AF_INET,
# type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9000),
# raddr=('127.0.0.1', 51123)>

#('127.0.0.1', 53692)
print(addr)

#5. 写收发数据的逻辑
"""
1kb = 1024B
1024kb = 1024 * 1024B
1mb = 1100000000
一发一收是一对,发和收要一一匹配
recv(字节)
"""

#接收数据 recv后面的字节数，是一次性最大接收这么多个字节
msg = conn.recv(1024)
print(msg.decode('utf-8'))

#发送数据
conn.send('你是个好人'.encode())

#四次挥手
conn.close()

#退还端口
sk.close()