# ### 守护进程
from multiprocessing import Process
import time

'''
守护进程语法：
进程对象.daemon = True
设置该进程对象是为守护进程
守护进程需要在start()方法之前设置

守护进程为主程守护，主进程如果代码执行完毕了，该守护进程自动终止
但其他子进程全部执行完毕之后，主进程彻底终止程序
'''

# 1.基本语法
"""
def func():
	print('子进程start')
	time.sleep(0.1)
	print('子进程end')


if __name__ == '__main__':
	p = Process(target=func)
	#在start开始之前设置该进程是守护进程
	p.daemon = True
	p.start()

	print('主进程执行结束')
"""

# 2.多个子进程的情况
"""
2个子进程 + 1个主进程
当主进程里面的代码全部执行完毕之后，守护进程自动终止
因为func2 这个任务进程没有执行完毕，所有主进程不能立刻终止程序


代码执行完毕
和程序执行完毕是两回事

代码执行完毕 意味着 守护进程立刻终止
只有非守护进程func2也都执行完毕之后，主进程才会真正的终止程序

func1 是守护进程
func2 是非守护进程，就是一个普通进程而已
默认主进程会等待所有进程执行完毕之后，才会最终终止程序
子进程和主进程彼此独立，数据也不共享，为了防止僵尸程序，才是等待的意义
"""
"""

def func1():
	count = 1
	while True:
		print('*' * count)
		time.sleep(0.5)
		count += 1


def func2():
	print('func2 start')
	time.sleep(3)
	print('func2 end')


if __name__ == '__main__':
	p1 = Process(target=func1)
	p1.daemon = True
	p2 = Process(target=func2)

	p1.start()
	p2.start()

	time.sleep(1)
	print('主进程代码执行完毕')
"""


# 3.守护进程的实际用途  报活
def alive():
	while True:
		print('1号服务主机。。i am ok')
		# 相隔0.5秒开始报活
		time.sleep(0.5)


def func():
	print('1号服务器主要负责统计mysql日志')
	time.sleep(10)
	print('1号服务器故障')


if __name__ == '__main__':
	p1 = Process(target=alive)
	p1.daemon = True
	p1.start()

	p2 = Process(target=func)
	p2.start()

	#用join 添加一下阻塞，如果join 执行结束了，就代表服务器统计日志的功能失效了
	#或者服务器崩溃，机器也会终止程序，终止报活
	p2.join()

	print('。。。。。。')
