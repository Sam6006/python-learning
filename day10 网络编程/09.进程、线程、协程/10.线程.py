# ### 线程
from threading import Thread
from multiprocessing import Process
import time, os, random

# 1.一个进程可以有多个线程，这些线程共享同一份资源
'''线程是异步并发程序'''
'''

def func(num):
	time.sleep(random.uniform(0.1, 1))
	print('子线程', num, os.getpid())


if __name__ == '__main__':
	for i in range(10):
		t = Thread(target=func, args=(i,))
		t.start()
'''

# 2. 并发多线程 和并发我进程  速度对比？ 多线程更快
"""
def func(i):
	print('子线程', i, os.getpid())


if __name__ == '__main__':
	lst = []
	# 1.计算多线程的时间
	start_time = time.perf_counter()
	for i in range(1000):
		t = Thread(target=func, args=(i,))
		t.start()
		lst.append(t)

	for i in lst:
		i.join()

	end_time = time.perf_counter()
	print(end_time - start_time, '主线程执行结束======>')  # 0.2335065

	# 计算多进程的时间
	lst = []
	start_time = time.perf_counter()
	for i in range(1000):
		p = Process(target=func, args=(i,))
		p.start()
		lst.append(p)

	for i in lst:
		i.join()

	end_time = time.perf_counter()
	print(end_time - start_time, '主进程执行结束=====>')  # 81.1386278
"""

# 3. 多线程之间共享同一份进程资源
num = 100
lst = []


def func(i):
	global num
	num -= 1


for i in range(100):
	t = Thread(target=func, args=(i,))
	t.start()
	lst.append(t)
# i.join 可以保证每一个线程都执行一遍，然后再打印num
for i in lst:
	i.join()

print(num)

# 4. 线程相关函数
'''
线程.is_alive()    检测线程是否仍然存在
线程.setName()     设置线程名字
线程.getName()     获取线程名字
1.currentThread().ident 查看线程id 号
2.enumerate()     返回目前正在运行的线程列表
3.activeCount()   返回目前正在运行的线程数据
'''


def func():
	time.sleep(3)


t = Thread(target=func)
t.start()

# is_alive()
print(t.is_alive())

# setName()
t.setName('李杰用脑过度')
print(t)
print(t.getName())

# 1.currentThread().ident 查看线程id号
from threading import currentThread


def func():
	print('子线程：', currentThread().ident)


t = Thread(target=func)
t.start()
print('主线程：', currentThread().ident, os.getpid())
# 2.enumerate()        返回目前正在运行的线程列表
from threading import enumerate
def func():
	print('子线程', currentThread().ident)
	time.sleep(0.5)

for i in range(10):
	t = Thread(target=func)
	t.start()

print(enumerate())
print(len(enumerate()))

# 3.activeCount()      返回目前正在运行的线程数量
from threading import activeCount
def func():
	print('子线程', currentThread().ident)
	time.sleep(0.5)

for i in range(10):
	Thread(target=func).start()

print(activeCount())