# ### event事件
import random
import time
from multiprocessing import Process, Event

'''
#阻塞事件
	e = Event() 生成事件对象e
	e.wait() 动态给程序加阻塞， 程序当中是否阻塞完全取决于该对象中的is_set(), 默认返回False
	
	如果是True, 不加阻塞
	如果是False 加阻塞
	
控制属性的值
	set() 方法，   将这个属性的值改成True
	clear() 方法   将这个属性的值改成False
	is_set() 方法  获取当前属性值是True还是False
	
'''
"""
# 基本语法
e = Event()
print(e.is_set())
# e.wait()
# 最多阻塞时间为1秒
e.wait(1)
print(1)
"""

"""
e = Event()
#将内部的一个属性改成True
e.set()
e.wait()
print(111)
#将内部的一个属性改成False
e.clear()
e.wait()
print(222)
"""
# 模拟交通灯的效果
def traffic_light(e):
	#默认红灯先亮
	print('红灯亮')
	while True:
		if e.is_set():
			#当前是绿灯，等待1秒
			time.sleep(1)
			print('红灯亮')
			e.clear()

		else:
			#当前是红灯
			time.sleep(1)
			#等待1秒之后，变成绿灯
			print('绿灯亮')
			e.set()

# e = Event()
# traffic_light(e)

# 模拟小车遇到红灯停,绿灯行的操作
def car(e,i):
	#e.is_set() 默认返回是False， 代表的是红灯
	if not e.is_set():
		print('car %s在等待' % i)
		e.wait()
	print('car %s通行了' % i)

'''
if __name__ == '__main__':
	e = Event()
	#模拟启动交通灯
	p1 = Process(target=traffic_light, args=(e,))
	p1.daemon = True
	p1.start()

	#模拟20辆小车
	for i in range(20):
		time.sleep(random.uniform(0,1))
		p2 = Process(target=car, args=(e, i))
		p2.start()

	print('程序彻底结束')
'''
# 优化版 : 等小车全都跑完之后,再让程序彻底终止
if __name__ == '__main__':
	lst = []
	e = Event()
	#模拟启动交通灯
	p1 = Process(target=traffic_light, args=(e,))
	# 设置红绿灯为守护进程,灯小车跑完,也终止红绿灯;
	p1.daemon = True
	p1.start()

	#模拟20辆小车
	for i in range(20):
		# 小车创建的速度太快,所以加一点延迟效果,生动表现出小车的行为;
		time.sleep(random.uniform(0,1))
		p2 = Process(target=car, args=(e, i))
		p2.start()
		lst.append(p2)

	# 等到小车都跑完之后,再去终止红绿灯;加一个等待;
	for i in lst:
		i.join()

	print('程序彻底结束')









