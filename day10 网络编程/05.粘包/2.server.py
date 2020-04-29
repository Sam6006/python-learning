import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

conn, addr = sk.accept()

#收发逻辑
#告诉接收端，我要发送的数据 长度是多少
conn.send('6'.encode('utf-8'))
#发送实际数据
conn.send('hello,'.encode('utf-8'))
conn.send('world,'.encode('utf-8'))

conn.close()
sk.close()