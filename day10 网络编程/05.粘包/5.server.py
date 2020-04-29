import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

conn,addr = sk.accept()

#收发数据逻辑
inp = input('请输入msg>>>：')
msg = inp.encode('utf-8')

#把这个长度的数据转化成二进制字节流，然后发送给对面，按照这么大的长度进行截取
res = struct.pack('i', len(msg))
conn.send(res)
conn.send(msg)
conn.send('world'.encode('utf-8'))

# 四次挥手
conn.close()
# 退还端口
sk.close()