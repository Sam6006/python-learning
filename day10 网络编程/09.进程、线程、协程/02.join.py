# ### join 功能，等待子进程执行完毕之后，主进程序再向下执行
from multiprocessing import Process
import time, os
"""
场景在多任务当中
同步:必须等我这件事干完了,你在干,只有一条主线,就是同步
异步:没等我这件事情干完,你就在干了,有两条主线,就是异步
阻塞:比如代码有了input,就是阻塞,必须要输入一个字符串,否则代码不往下执行
非阻塞:没有任何等待,正常代码往下执行.
 
# 同步阻塞  :效率低,cpu利用不充分
# 异步阻塞  :比如socketserver,可以同时连接多个,但是彼此都有recv
# 同步非阻塞:没有类似input的代码,从上到下执行.默认的正常情况代码
# 异步非阻塞:效率是最高的,cpu过度充分,过度发热



"""
# 1.join基本用法
"""
def func():
	print('发送第一封邮件')

if __name__ == '__main__':
	p = Process(target=func)
	p.start()
	#time.sleep(1)
	'''针对于p进程对象来说，必须等待p这个进程任务执行完毕之后，主进程的代码再向下执行'''
	p.join()
	print('发送第二封邮件')
"""

# 2.多个子进程通过join加阻塞，可以实现同步控制
"""
def func(index):
	print('第%s封邮件已经发送...' % (index))


if __name__ == '__main__':
	lst = []
	for i in range(10):
		# 创建进程，1个主进程，10个子进程，共11个进程，创建的是异步程序，加上join是同步程序
		p = Process(target=func, args=(i,))
		# 调用进程
		p.start()
		lst.append(p)
		# 如果把join加到循环里，当前这个进程对象.join必须执行结束，下一个进程对象才能创建,
		# 变成了同步程序,而进程的提出是为了提升执行的速度;
		#p.join()
	# 循环列表中的每一个进程对象,都加上一个join,可以让所有的进程对象都执行完毕,
	# 就释放阻塞往下执行;保证子进程和主进程之间的同步性;
	for i in lst:
		i.join()
	print('发送最后一封邮件')

"""
# 使用第二种方法创建进程
'''用自己定义类的方式创建进程'''


# 1.基本使用
# 必须继承父类  Process 类
class MyProcess(Process):
	# 类似于handle，必须写run方法
	def __init__(self, arg):
		# 必须调用一下父类的初始化方法
		super().__init__()
		# 把参数通过arg来进行保存
		self.arg = arg

	# 类似于handle，必须写成run方法
	def run(self):
		print('子进程%s, 父进程%s' % (os.getpid(), os.getppid()))
		print(self.arg)


if __name__ == '__main__':
	lst = []
	# 进程的并发是异步程序
	for i in range(10):
		p = MyProcess('参数:%s' % (i))
		p.start()
		lst.append(p)
	# 等待所有子进程结束再执行主进程代码是同步程序
	for i in lst:
		i.join()
	print('最后打印子进程id', os.getpid())
