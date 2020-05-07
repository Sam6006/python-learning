# ### 线程队列
from queue import Queue

'''
put 往线程队列中放值
get 从线程队列中取值
put_nowait 如果放入的值，长度超过了队列的长度，直接报错
get_nowait 如果获取的值，已经没有了，直接报错
'''
# 1.queue 先进先出
q = Queue()
q.put(11)
q.put(22)
print(q.get())
print(q.get())

# q.get()  发生阻塞
# q.get_nowait()  queue.Empty 没有值了，直接报错

# 指定队列长度
q2 = Queue(2)
q2.put(111)
q2.put(333)
# q2.put(444)  发生阻塞
# q2.put_nowait(333) queue.Full 已满，直接报错

# 2 lifoQueue 后进先出（数据结构中，内存栈队列的一种存储结构
from queue import LifoQueue

lq = LifoQueue()
lq.put(111)
lq.put(222)
print(lq.get())
print(lq.get())

# 3.priorityQueue 按照优先级顺序排序
from queue import PriorityQueue

'''
默认按照数字大小排序
如果是字母，会按照ascii编码大小进行排序，从小到大
先写先排

'''
pq = PriorityQueue()
pq.put(12, "zhangsan")
pq.put(6, "lisi")
pq.put(18, "zhaoliu")
pq.put(18, "wangwu")

print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())

#单一的一个元素，只能是同一类型  数字
pq = PriorityQueue()
pq.put(13)
pq.put(18)
pq.put(3)
print(pq.get())
print(pq.get())
print(pq.get())

# 单一的一个元素,只能是同一类型 字符串
pq = PriorityQueue()
pq.put("acc")
pq.put("aa")
pq.put("z")

print(pq.get())
print(pq.get())
print(pq.get())
