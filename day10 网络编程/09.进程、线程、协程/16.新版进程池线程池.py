# ### 新版进程池，线程池
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import current_thread as cthread
import os, time

# 1.进程池，可以允许cup并行
"""
def func(i):
	print('Process:', i, os.getpid())
	time.sleep(2)
	print('Process:end',os.getpid())
	return 5488


if __name__ == '__main__':
	# cpu_count 获取的是逻辑处理器
	#print(os.cpu_count())
	# 1.创建进程池对象
	'''最多默认创建cpu_count这么多个进程执行任务，只创建4个进程来执行所有任务，不会再有额外的进程创建出来了'''
	p = ProcessPoolExecutor(os.cpu_count())
	# 2.异步触发进程
	# res = p.submit(func,1) #<Future at 0x1c6ee89e908 state=running> 该对象存放了函数的返回值
	# print(res)

	# 多个任务
	for i in range(10):
		res = p.submit(func, i)

	# 3 获取进程任务的返回值
	res2 = res.result()
	print(res2)
	# 4 shutdown 等到所有子进程执行完毕之后，再向下执行，相当于join
	p.shutdown()
	print('主进程执行完毕')
"""
# (2) 线程池 , as 相当于起一个别名
"""

def func(i):
	print('thread', i, cthread().ident)
	time.sleep(2)
	print('thread %s end' % i)

#max_workers = (os.cpu_count() or 1)  * 5 默认值是cpu逻辑核心数*5
'''最多默认创建(os.cpu_count() or 1) * 5 这么多个线程执行任务，不会再有额外的线程创建'''
tp = ThreadPoolExecutor()
for i in range(50):
	tp.submit(func, i)

tp.shutdown()
print('主线程执行完毕')
"""

# 3 线程池的返回值
"""
def func(i):
	#打印线程号
	print('thread',i, cthread().ident)
	time.sleep(3)
	return cthread().ident

tp = ThreadPoolExecutor()  #max_workers = (os.cpu_count() or 1) *5
lst = []
setvar = set()
for i in range(10):
	res = tp.submit(func,i)
	#把对象都塞到列表里面，如果直接获取值出现阻塞，就不能异步并发，所有都放列表中，统一处理
	lst.append(res)
	#print(res.result())

for i in lst:
	#获取该线程对象的返回值
	print(i.result())
	setvar.add(i.result)

print(setvar)
print('主线程执行完毕')
"""


# 4. map返回迭代器，线程池版本的高阶函数map, 升级的map版本
def func(i):
	time.sleep(0.2)
	print('thread', i, cthread().ident)
	print('thread end %s' % i)
	return '*' * i


tp = ThreadPoolExecutor(os.cpu_count())
it = tp.map(func, range(20))
tp.shutdown()
print('主线程执行结束')

from collections import Iterator, Iterable

res = isinstance(it, Iterator)
print(res)

print(list(it))
