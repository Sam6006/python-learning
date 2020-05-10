# ### JD Server

import socket
sk = socket.socket()

sk.bind(('127.0.0.1', 8080))
sk.listen()
### http协议特点:
'''
​    (1)  基于TCP/IP
​    (2) 基于请求响应协议
​    (3) 无连接或者短连接
​    (4) 无状态保存
'''

### http请求协议
'''
URL：协议：//域名：端口/路径？参数
https://www.jd.com/？a=1

get url的路径部分？数据   协议                      # 请求首行
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likGecko)Chrome/74.0.3729.131 
accept-encoding: gzip, deflate, br
空行
请求体 # 只有post请求才有请求体
'''

###  响应协议格式
'''
协议  200 OK  # 响应首行
content-length: 20636
content-type: text/html; charset=utf-8
date: Sun, 08 Sep 2019 04:24:58 GMT
空行
响应体
'''
while 1:
	#  等待链接
	print('server is waiting....')
	conn, addr = sk.accept()
	#接受客户端请求信息
	data = conn.recv(1024)
	print('data>>>', data.decode('utf-8'))
	#相应页面
	with open('index.html', 'rb') as f:
		html = f.read()
	conn.send(b'HTTP/1.1 200 OK\r\n\r\n%s' %html)