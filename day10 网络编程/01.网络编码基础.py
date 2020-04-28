
# 1.网络基础相关的知识

	#1 架构
		#a. C / S架构: client客户端 和 server服务器端
			# 优势: 能充分发挥PC机的性能
		# b. B / S架构: browser浏览器和server服务器 隶属于C / S架构
			# B / S架构 统一了应用的接口.
	# (2)通信的事:
		# a.同一台电脑上两个py程序通信: 打开一个文件
		# b.两个电脑如何通信: 连一个网线
		# c.多个电脑通信:
			# ex: 电脑1(源) 要找电脑2(目标)
			# 电脑1首先发送一个请求帧, 期中包含(我的ip是192.168.1.1, 我的mac地址是xxxxxxxx, 我要找ip地址为192.168.1.2的主机),
			# 将此请求发送给交换机.交换机要广播这条消息给其他所有的主机,
			# 目标主机接收到消息后, 对比发现自己就是被找的主机, 回复给交换机信息(我的ip地址是192.168.1.2,
			# 我的mac地址是yyyyyyyyy, 请回复给ip地址为192.168.1.1,mac地址为xxxxxxx的主机)
			# 交换机单播形式返回给源主机

		# 知识点:
			# 1 mac地址: 是一个物理地址, 全球唯一, 类似于身份证
			# 2 ip地址: 是一个四位点分十进制, 它标识了计算机在网络中的位置.类似于  学号
			# 3 交换机的通信方式:
					# 广播: 吼一嗓子
					# 单播: 一对一
					# 组播: 一对多
			#4 arp协议: 通过目标ip地址获取目标mac地址的一个协议.
			#5 端口: 操作系统为本机上每一个运行的程序都随机分配一个端口, 其他电脑上的程序可以通过端口获取到这个程序
				# ip地址 + 端口 能唯一找到某台电脑上的某一个服务程序
			#6 路由器: 连接不同网段, 路由
			#7 网关: 类似于一个局域网的出口和入口
			#8 网段: 一个局域网内的ip地址范围
			#9 子网掩码: 子网掩码 & ip地址   得到网段
			#10 osi五层模型:
				# 应用层: http, https, ftp
				# 传输层: tcp / udp          四层交换机 四层路由器
				# 网络层: ip协议              路由器 三层交换机
				# 数据链路层: arp协议         以太网交换机 网卡 网桥
				# 物理层: 传输电信号           集线器 网线 光纤

# 2 socket模块
	# 这是一个新的模块 import socket
	# socket 又叫做套接字
	# 有很多种类型, 但是咱们只需要知道两种就可以了
	# sk = socket.socket(family=AF_INET, type=SOCK_STREAM)
# family:
	# 一种: AF_UNIX基于文件类型的套接字(早期socket是源自于unix系统而研发的一个功能, 主要是为了同一台电脑上, 多个程序直接通信)
	# unix系统的中心思想是: 一切皆文件
	# 一种: AF_INET基于网络类型的套接字
# type:
	# 一种是基于TCP协议 SOCK_STREAM
	# 一种是基于UDP协议 SOCK_DGRAM

# tcp 协议: 可靠的, 面向连接的, 面向字节流形式的传输方式
# udp协议: 不可靠的, 不面向连接的, 面向数据报的传输方式, 但是它快

# 重点顺序:
# arp协议
# 路由器与交换机的区别?
# tcp协议和udp协议的特点, 及tcp协议的编码
# 软件开发架构
# osi五层模型
