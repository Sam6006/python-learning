# ### client

import socket

#1.创建udp对象 type = SOCK_DGRAM 代表udp协议
sk = socket.socket(type=socket.SOCK_DGRAM)

#2.sendto（要发的消息,(ip,端口)）
sk.sendto('你好'.encode('utf-8'), ('127.0.0.1',9000))

#3.关闭udp连接
sk.close()