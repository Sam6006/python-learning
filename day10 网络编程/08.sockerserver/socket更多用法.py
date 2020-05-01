# 服务端套接字函数
# s.bind()    绑定(主机,端口号)到套接字
# s.listen()  开始TCP监听
# s.accept()  被动接受TCP客户的连接,(阻塞式)等待连接的到来
#
# 客户端套接字函数
# s.connect()     主动初始化TCP服务器连接
# s.connect_ex()  connect()函数的扩展版本,出错时返回出错码,而不是抛出异常
# (等价于:异常处理+connect 一旦网络不通,作用:返回错误号而不是直接报错)
#
# 公共用途的套接字函数
# s.recv()            接收TCP数据
# s.send()       发送TCP数据,send返回值是发送的[字节数量],这个值可能小于要发送的string字节数
# s.sendall()    发送TCP数据,sendall返回值是None,发送string所有数据
# '''
# # 下面两个代码等价:
#     #sendall => sock.sendall('Hello world\n')
#     #send => buffer = 'Hello world\n'
#              while buffer:
#         		n = sock.send(buffer)
#         		buffer = buffer[n:] (切片)
# '''
# s.recvfrom()        接收UDP数据
# s.sendto()          发送UDP数据
# s.getpeername()     连接到当前套接字的远端的地址
# s.getsockname()     当前套接字的地址
# s.getsockopt()      返回指定套接字的参数
# s.setsockopt()      设置指定套接字的参数
# s.close()           关闭套接字
#
# 面向锁的套接字方法
# s.setblocking()     设置套接字的阻塞与非阻塞模式
# s.settimeout()      设置阻塞套接字操作的超时时间
# s.gettimeout()      得到阻塞套接字操作的超时时间
#
# 面向文件的套接字的函数
# s.fileno()          套接字的文件描述符
# s.makefile()        创建一个与该套接字相关的文件
#
# 更多方法