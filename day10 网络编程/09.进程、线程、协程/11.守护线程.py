# ### 守护线程： 等待所有线程执行结束之后，再自动结束， 守护所有线程
from threading import Thread
import time

def func1():
	while True:
		time.sleep(0.5)
		print('我是线程1， func1任务')

def func2():
	print('我是线程2，start')
	time.sleep(3)

#启动线程1
'''线程可以选择不加if __name == "__main__": 因为线程共享同一份资源， 当然加上更好 '''

t1 = Thread(target=func1)
#设置守护线程
t1.setDaemon(True)
t1.start()

t2 = Thread(target=func2)
t2.start()

print('主线程执行结束')