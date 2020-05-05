# ### 进程队列
from multiprocessing import Process, Queue
#1 基本用法
'''
先进先出，后进后出
功能：让进程之间形成数据之间的共享
'''

"""
q = Queue()
#1. 把数据放到q队列中  put
q.put(111)
#2. 把数据从队列中取出来  get
res = q.get()
print(res)
#3. 当队列里面的值都拿出来了，已经没有数据的时候，再获取就会出现阻塞
#res = q.get()
#4.get_nowait() 无论有没有都去拿数据，如果拿不到，直接报错
#res = q.get_nowait() #queue.Empty

# 抑制get_nowait 报错 用try 方法实现
try:
	res = q.get_nowait()
except:
	print('没有数据拿咯')
"""

#2 可以使用queue 指定队列长度
"""
q = Queue(3)
q.put(11)
q.put(22)
q.put(33)
#print(q.get())
#q.put(44)  #阻塞，如果队列已存满，再放值直接阻塞
#无论如何都往队列中存值，如果存满直接报错
#q.put_nowait(555) #queue.Full
try:
	q.put_nowait(555)
except:
	print('队列数据满了，放不下了')
"""

#3. 进程之间的通讯 依赖Queue
#子进程
def func(q):
	#2. 子进程获取数据
	res = q.get()
	print('子进程获取的数据..',res)

	#3. 子进程添加数据
	q.put('cccc')


if __name__ == '__main__':
	q = Queue()
	p = Process(target=func, args=(q,))
	p.start()

	#1.主进程添加数据
	q.put('abc')
	p.join()
	#4.主进程获取数据
	res = q.get()
	print('主进程获取的数据..',res)
	print('程序结束')



















