# ### 客户端
import socket
sk = socket.socket()
sk.connect( ("127.0.0.1",9000) )
# 收发数据逻辑
sk.close()