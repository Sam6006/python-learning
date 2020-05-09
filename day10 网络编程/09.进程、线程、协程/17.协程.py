# ### 协程
import gevent, time

"""
def gen():
	for i in range(10):
		yield i

#初始化生成器函数，返回生成器对象，简称生成器
mygen = gen()
for i in mygen:
	print(i)

"""
# 1.用协程改写生产者消费者模型
'''
def producer():
	for i in range(100):
		yield i

def consumer():
	g = producer()
	for i in g:
		print(i)

consumer()
'''
# 2 协程的具体实现
'''
switch 遇到阻塞时，可以手动调用该函数进行任务的切换
缺点：不能自动规避io，即不能自动实现遇到阻塞就切换，只能手动
'''
"""
import time
from greenlet import greenlet


def eat():
	print('eat one')
	g2.switch()
	time.sleep(1)
	print('eat two')


def play():
	print('play one')
	time.sleep(1)
	print('play two')
	g1.switch()


g1 = greenlet(eat)
g2 = greenlet(play)
g1.switch()
"""
# 3.gevent 缺陷:不能够识别一些阻塞


'''spawn 类似于switch 遇到阻塞可以自动进行任务的切换'''
"""

def eat():
	print('eat one')
	time.sleep(1)
	print('eat two')


def play():
	print('play one')
	time.sleep(1)
	print('play two')


# 利用gevent.spawn创建协和对象g1
g1 = gevent.spawn(eat)
# 利用gevent.spwan创建协程对象p2
g2 = gevent.spawn(play)

g1.join()
g2.join()
print('主线程执行完毕')
"""

# 4.进阶改造，用gevent.sleep 取代time.sleep()
# 自动实现任务切换功能
"""
def eat():
	print('eat one')
	gevent.sleep(1)
	print('eat two')


def play():
	print('play one')
	gevent.sleep(1)
	print('play two')


# 利用gevent.spawn创建协和对象g1
g1 = gevent.spawn(eat)
# 利用gevent.spwan创建协程对象p2
g2 = gevent.spawn(play)

g1.join()
g2.join()
print('主线程执行完毕')
"""
# 5.终极改造， 彻底解决不识别阻塞问题
from gevent import monkey

# mokey.patch_all 可以把下面引入的所有模块中的阻塞，重新识别出来
monkey.patch_all()


def eat():
	print('eat one')
	time.sleep(1)
	print('eat two')


def play():
	print('play one')
	time.sleep(1)
	print('play two')


# 利用gevent.spawn创建协和对象g1
g1 = gevent.spawn(eat)
# 利用gevent.spwan创建协程对象p2
g2 = gevent.spawn(play)

g1.join()
g2.join()
print('主线程执行完毕')
