# ### 生产者与消费者模型

'''
#爬虫例子
1号进程负责爬取网页中所有内容
2号进程负责匹配提取网页中的关键字

1号进程就可以看成一个生产者
2号进程就可以看成一个消费者

有时可能生产者比消费者快，或者慢
所以为了减少生产者和消费者速度上的差异化，加了一个中间的缓冲队列

比较理想的模型，两者之间的速度相对平均
生产者和消费者模型从程序上来看，就是存数据和取数据之间的过程
'''
from multiprocessing import Process, Queue
import time, random


# 消费者模型（负责取值)
def consumer(q, name):
	while True:
		# 拿出数据
		food = q.get()
		# 如果取的数据是None, 代表已经拿到最后一个数据了，到头了，这个时候将循环结束
		if food is None:
			break
		time.sleep(random.uniform(0.1, 1))
		print('%s 吃了一个 %s' % (name, food))


# 生产者模型（负责存值)
def producer(q, name, food):
	for i in range(3):
		time.sleep(random.uniform(0.1, 1))
		print('%s 生产了 %s' % (name, food))
		q.put(food + str(i))


if __name__ == '__main__':
	q = Queue()
	# 消费者
	c1 = Process(target=consumer, args=(q, 'alex'))
	c1.start()

	# 生产者
	p1 = Process(target=producer, args=(q, 'sam', '面包'))
	p1.start()

	#等待生产者把所有数据生产完毕，保证队列里面有3个数据
	p1.join()
	q.put(None)