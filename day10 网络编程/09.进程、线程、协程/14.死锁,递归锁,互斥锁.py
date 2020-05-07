# ### 死锁,递归锁,互斥锁
from threading import Thread, Lock, RLock
import time

lock = Lock()

# ### 1.死锁现象， 只上锁不解锁是死锁
'''
lock.acquire()
lock.acquire()
print(123)
'''

# 逻辑上的死锁现象
"""

noodle = Lock()
kuazi = Lock()

def eat1(name):
	noodle.acquire()
	print('%s 拿到面条' % name)
	kuazi.acquire()
	print('%s 拿到筷子' % name)

	print('开始吃面')
	time.sleep(0.5)

	kuazi.release()
	print('%s 放下筷子' % name)
	noodel.release()
	print('%s 放下面条' % name)


def eat2(name):
	kuazi.acquire()
	print('%s 拿到筷子' % name)
	noodel.acquire()
	print('%s 拿到面条' % name)

	print('开始吃面')
	time.sleep(0.5)

	noodel.release()
	print('%s 放下面条' % name)
	kuazi.release()
	print('%s 放下筷子' % name)


if __name__ == '__main__':
	name_lst1 = ['Alex', 'Sam', 'John']
	name_lst2 = ['nick', 'amanda', 'youku']

	for name in name_lst1:
		Thread(target=eat1, args=(name,)).start()

	for name in name_lst2:
		Thread(target=eat2, args=(name,)).start()
"""
# ###2.递归锁
'''上几把锁，就对应几个解锁，无论上了几把锁，只要解锁的数量相同即可 就可以解锁
针对于应急情况下的解锁;

	递归锁专门用于解决死锁现象
	临时用于快速解决服务区崩溃死锁的问题
'''
rlock = RLock()


def func():
	rlock.acquire()
	rlock.acquire()
	rlock.acquire()
	print(111)
	rlock.release()
	rlock.release()
	rlock.release()
	print(222)


func()

# 解决吃面条问题
# noodle = Lock()
# kuazi = Lock()
"""
noodle = kuazi = RLock()
def eat1(name):
	noodle.acquire()
	print('%s 拿到面条' % name)
	kuazi.acquire()
	print('%s 拿到筷子' % name)

	print('开始吃面')
	time.sleep(0.5)

	kuazi.release()
	print('%s 放下筷子' % name)
	noodle.release()
	print('%s 放下面条' % name)


def eat2(name):
	kuazi.acquire()
	print('%s 拿到筷子' % name)
	noodle.acquire()
	print('%s 拿到面条' % name)

	print('开始吃面')
	time.sleep(0.5)

	noodle.release()
	print('%s 放下面条' % name)
	kuazi.release()
	print('%s 放下筷子' % name)


if __name__ == '__main__':
	name_lst1 = ['Alex', 'Sam', 'John']
	name_lst2 = ['nick', 'amanda', 'youku']

	for name in name_lst1:
		Thread(target=eat1, args=(name,)).start()

	for name in name_lst2:
		Thread(target=eat2, args=(name,)).start()
"""

# ### 互斥锁
'''
	从语法上来说，锁可以互相嵌套，但是不要使用
	上一次锁，就对应解开一把锁，形成互斥锁
	吃面条和拿筷子是同时的，上一把锁就够了，不需要分开上锁
'''
mylock = Lock()


# 正确逻辑
def eat1(name):
	mylock.acquire()
	print('%s 拿到面条' % name)
	print('%s 拿到筷子' % name)
	print('开始吃面')
	time.sleep(0.5)

	print('%s 放下筷子' % name)
	print('%s 放下面条' % name)
	mylock.release()


def eat2(name):
	mylock.acquire()
	print('%s 拿到筷子' % name)
	print('%s 拿到面条' % name)
	print('开始吃面')
	time.sleep(0.5)

	print('%s 放下面条' % name)
	print('%s 放下筷子' % name)
	mylock.release()


if __name__ == '__main__':
	name_lst1 = ['Alex', 'Sam', 'John']
	name_lst2 = ['nick', 'amanda', 'youku']

	for name in name_lst1:
		Thread(target=eat1, args=(name,)).start()

	for name in name_lst2:
		Thread(target=eat2, args=(name,)).start()
