# ### pickle 序列化模块
import pickle

'''
序列化：
	把不能够直接存储的数据变得可存储
反序列化：
	把数据恢复成原本的数据格式
	
serialize  序列化
unserialize 反序列化
'''

# dump的结果是bytes,dump用的f文件句柄需要以wb的形式打开,load所用的f是'rb'模式
# 支持几乎所有对象的序列化
# 对于对象的序列化需要这个对象对应的类在内存中
# 对于多次dump/load的操作做了良好的处理

#正常情况下，不能够直接把容器类型数据直接存储在文件中
"""
with open("ceshi.txt",mode="w",encoding="utf-8") as fp:
	lst = [1,2,3]
	fp.write(lst) #	TypeError: write() argument must be str, not list
"""

#dumps 把任意对象序列化成一个bytes
lst = [1,2,3,4,5]
res = pickle.dumps(lst)
print(res) #b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04K\x05e.'

#loads 把任意bytes反序列化成原来 数据
res = pickle.loads(res)
print(res, type(res))

#序列化函数
def func():
	print('我是一个函数')

res = pickle.dumps(func)
print(res)

#反序列化函数
fu = pickle.loads(res)
fu()
# 序列化迭代器
from collections import Iterable, Iterator
it = iter(range(10))
print(isinstance(it, Iterator))

res = pickle.dumps(it)
print(res)

res = pickle.loads(res)
print(res)
print(list(res))

#dumps 和 loads 把数据存储在文件
setvar = {"a","b"}
with open("ceshi.txt",mode="rb+") as fp:
	res = pickle.dumps(setvar)
	fp.write(res)

	#读取内容的时候，先把光标移动的文件行首
	fp.seek(0)
	res = fp.read()
	print(res)
	res = pickle.loads(res)
	print(res)


#dump 把对象序列化后写入到file-like object(文件对象)
def func2():
	print('我是func2')

with open('ceishi02.txt', 'wb') as f:
	# 参数1： 要序列化的数据， 参数2 对应的文件对象
	pickle.dump(func2, f)

#load  把file-like Object(即文件对象)中的内容拿出来,反序列化成原来数据
with open("ceishi02.txt",mode="rb") as fp:
	fun = pickle.load(fp)

fun()

# pickle模块可以序列化所有的数据类型.












