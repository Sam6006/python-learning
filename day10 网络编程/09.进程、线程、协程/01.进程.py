#  ### 进程

# 获取进程号 ===查当于人的身份证，是唯一值
'''
并发:一个cpu同一时间不停执行多个程序
并行:多个cpu同一时间不停执行多个程序

'''
import os

'''
#获取当前进程id  当前子进程
res = os.getpid()
print(res)

#获取父进程id
res = os.getppid()
print(res)
'''
# 1.进程的基本用法
from multiprocessing import Process
import time

"""
def func():
	print('2222,当前子进程id>>:%s, 它的父进程id>>>:%s' % (os.getpid(), os.getppid()))


if __name__ == "__main__":
	print('111,子进程id>>>：%s， 父进程id>>%s' % (os.getpid(), os.getppid()))

	# 创建子进程
	'''target =函数 单独用一个进程去执行谁，去完成哪个任务'''
	p = Process(target=func)
	# 调用子进程
	p.start()
"""

# 2.带有参数的函数
'''
异步程序：不等每一行代码执行结束，就往下执行其他代码是异步程序
创建进程时候，需要从创建 -> 就绪， cpu才能过来执行就绪态的程序
创建进程时，需要分配空间，分配空间会出现阻塞现象
'''
"""
def func():
	for i in range(1, 5):
		print('<<222>>当前子进程id>>:%s,它的父进程id>>：%s' % (os.getpid(), os.getppid()))


if __name__ == '__main__':
	print('111,子进程id>>>：%s， 父进程id>>%s' % (os.getpid(), os.getppid()))
	# 创建进程,返回进程对象
	p = Process(target=func)
	p.start()

	n = 5
	for i in range(1,n+1):
		print('*' * i)
"""

"""
def func(n):
	for i in range(1, n + 1):
		time.sleep(0.1)
		print('<<222>>当前子进程id>>:%s,它的父进程id>>：%s' % (os.getpid(), os.getppid()))


if __name__ == '__main__':
	print('111,子进程id>>>：%s， 父进程id>>%s' % (os.getpid(), os.getppid()))
	# args(value1,value2....) args类型是元组
	n = 5
	p = Process(target=func, args=(n,))
	p.start()

	for i in range(1, n + 1):
		time.sleep(0.1)
		print('*' * i)
"""
# 3.进程之间数据，彼此是隔离的
'''
count = 99


def func():
	global count
	count += 1
	print("当前子进程id号%s" % (os.getpid()), count)


if __name__ == '__main__':
	# 创建进程
	p = Process(target=func)
	# 调用进程
	p.start()
	# 为了先让子进程跑完，再执行主进程中的count, 看看是否通过子进程进行了修改
	time.sleep(1)
	print('我是主进程', count)
'''
# 4.多进程之间的并发
'''
在程序并发时，因为cpu的调度策略问题，不一定谁先执行，谁后执行
但是如果遇到阻塞一定会进行切换，任务的执行是互相抢占cpu资源的过程
以目前程序来看，主进程执行的稍快，子进程执行稍慢
主进程和子进程齐头并进行往前跑，谁跑在前后说不准，依赖cpu的调度策略
'''

'''
def func(args):
	print(">>222>>当前子进程id>>:%s,它的父进程id>>:%s" % (os.getpid(), os.getppid()))
	print("end", args)


if __name__ == '__main__':
	for i in range(10):
		Process(target=func, args=(i,)).start()

	print('主进程执行结束')
'''

# (5) 主进程和父进程之间的关系
'''
主进程执行完所有代码之后，开始等待
等待所有子进程全部结束之后再彻底终止程序

如果等待，主进程终止了，子进程就会变成僵尸程序
在后台不停的运行，占用内存和cpu
因为进程数太多，不容易找到，也不容易管理
所以主进程跑完后，再彻底结束程序
'''
def func(args):
	print(">>222>>当前子进程id>>:%s,它的父进程id>>:%s" % (os.getpid(), os.getppid()))
	time.sleep(0.1)
	print("end", args)

if __name__ == '__main__':
	for i in range(10):
		Process(target=func,args=(i,)).start()

	print('主进程执行结束....')























