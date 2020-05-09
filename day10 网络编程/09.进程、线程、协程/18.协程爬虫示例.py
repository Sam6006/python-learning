# ### 协程爬虫示例

'''
1.spawn(函数，参数1，。。。。。) 启动一个协程任务
2.join() 阻塞，直到某个协程执行完毕之后，再打开阻塞
3.joinall() 等待所有协程执行完毕
	g1.join() g2.join() 可以通过joinall 简写
	gevent.joinall([g1,g2]) 等价于join  参数是一个列表

4. value 获取协程任务中的返回值，g1.value 获取g1对象中返回值

'''
"""
a = 1
b = 2
print(a,b)
#如果想要把两句代码放到一行，中间用分号;隔开
a = 1; b = 2
print(a,b)
"""

# 1 joinall  value 这两个函数用法
"""
from gevent import monkey; monkey.patch_all()
import time, gevent


def eat():
	print("eat one")
	time.sleep(1)
	print("eat two")
	return "吃完了"


def play():
	print("play one")
	time.sleep(1)
	print("playtwo")
	return "玩完了"

g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)

gevent.joinall([g1, g2])
print('主线程执行完毕')
print(g1.value)
print(g2.value)
"""
# 2.利用协程爬取网页数据

"""
HTTP 状态码：
	200 Ok
	400 bad request
	404 not found
"""
"""
#基本语法
#爬取网站信息， 返回响应对象
response = requests.get('http://www.baidu.com')
print(response)
#获取状态码
res = response.status_code
print(res)

#获取网页的字符编码集 apparent_encoding
res = response.apparent_encoding
print(res)

#设置编码集
response.encoding = res
#获取网页里面的内容
res = response.text
print(res)
"""
from gevent import monkey;

monkey.patch_all()
import gevent
import time
import requests


def get_result(url):
	"""
	任务函数
	:param url:
	"""
	res = requests.get(url)
	print(url, res.status_code)


url_1 = ['http://www.baidu.com',
		 'https://www.jd.com',
		 'http://www.taobao.com',
		 'http://www.qq.com',
		 'http://www.mi.com',
		 'http://www.cnblogs.com',
		'http://www.baidu.com',
		 'https://www.jd.com',
		 'http://www.taobao.com',
		 'http://www.qq.com',
		 'http://www.mi.com',
		 'http://www.cnblogs.com',
		'http://www.baidu.com',
		 'https://www.jd.com',
		 'http://www.taobao.com',
		 'http://www.qq.com',
		 'http://www.mi.com',
		 'http://www.cnblogs.com'
		 ]


def sync_func(url_1):
	for url in url_1:  # 串行执行任务函数
		get_result(url)


def async_func(url_1):
	'''异步'''
	l = []
	for url in url_1:
		g = gevent.spawn(get_result, url)  # 使用gevent，协程去并发实现执行任务函数
		# 当遇到请求某个网页发生比较大的网络延迟(io) 马上会切换到其他的任务函数
		l.append(g)
	gevent.joinall(l)  # 等待所有任务函数执行结束

# 串行执行任务函数
start_time = time.perf_counter()
sync_func(url_1)  #sync: 24.1470206
print('sync:', time.perf_counter() - start_time)

#协程，并发执行函数
start_time = time.perf_counter()
async_func(url_1)  #async: 0.5513688000000023
print('async:', time.perf_counter() - start_time)
