# ### 服务端
'''如果是udp的服务器，只能先接收数据，tcp服务端可以先发也可以先收'''

import socket

#1 创建udp对象， type = SOCK_DGRAM 代表udp协议
sk = socket.socket(type=socket.SOCK_DGRAM)
#2.绑定ip和端口（在网络中注册该主机)
sk.bind(("127.0.0.1",9000))

#3.udp服务器，第一次启动时，一定是先接收数据，再发送数据
msg, cli_addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
print(cli_addr)

#4.关闭udp连接
sk.close()
