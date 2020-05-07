# ### 线程的数据安全  依赖lock
'''用上锁的方法， 来保证数据安全， 代价就是会牺牲一点执行的速度'''
from threading import Thread, Lock
n = 0

def func1(lock):
	global n
	for i in range(100000):
		#方法一
		#上锁
		lock.acquire()
		n -= 1
		#解锁
		lock.release()

def func2(lock):
	global n
	for i in range(100000):
		'''with 语法  自动实现上锁, 解锁'''
		with lock:
			n += 1

if __name__ == '__main__':
	#创建一把锁
	lock = Lock()
	lst = []
	for i in range(10):
		t1 = Thread(target=func1, args=(lock,))
		t2 = Thread(target=func2, args=(lock,))
		t1.start()
		t2.start()

		lst.append(t1)
		lst.append(t2)

	for i in lst:
		i.join()

	print('主线程执行结束')
	print(n)