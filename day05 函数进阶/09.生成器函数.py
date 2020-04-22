# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/29 17:32
"""
# 生成器函数
'''
yield 类似于 return
共同点在于：执行到这句话都会把值返回出去
不同点在于：yield每次返回时，会记住上次离开时执行的位置，
下次再调用生成器，会从上次执行的位置往下走，而return直接终止函数，每次重头调用
yield 6 和 yield(6) 2种写法都可以 yield 6更像 return 6 的写法，推荐使用
'''
#1.基本语法
def func():
	print('one')
	yield 1

	print('two')
	yield 2

	print('three')
	yield 3
'''
初始化生成器函数返回生成器对象，简称生成器
第一次,通过next调用,执行print("one") , 记录当前的状态,返回yield 1,程序添加阻塞,等待下一次调用
第二次,通过next调用,执行print("two") , 记录当前的状态,返回yield 2,程序添加阻塞,等待下一次调用
第三次,通过next调用,执行print("three") , 记录当前的状态,返回yield 3,程序添加阻塞,等待下一次调用

第四次,通过next调用,因为没有yield 返回值了,所以直接越界报错 ... 

'''

#初始化生成器函数返回生成器对象，简称生成器
gen = func()
'''
#第一次调用
res = next(gen)
print(res)

print('=======')
#第二次调用
res = next(gen)
print(res)

print('=======')
#第三次调用
res = next(gen)
print(res)
'''

'''
# 调用第四次 error
res = next(gen)
print(res)
'''


#2.升级版生成器函数
def func():
	for i in range(100):
		yield '我的球衣号码是{:d}'.format(i)

#初始化生成器函数，返回生成器对象，简称生成器

gen = func()
'''
for i in range(30):
	res = next(gen)
	print(res)

#如果是极大数据量，通过for遍历等于执行死循环
for i in gen:
	print(i)

'''

#3.send 使用 send 只用给上一个yield发送数据
'''
send
next和send 区别
	next 只能取值
	send 不但能取值，还能发送值
send 注意点
	第一个send 不能给yield 传值  默认只能写None
	最后一个yield 接受不到send的发送值
'''


def mygen():
	print("start")
	res1 = yield 1
	print(res1, "<内头>")

	res2 = yield 2
	print(res2, "<内头>")

	res3 = yield 3
	print(res3, "<内头>")

	print("end")

#初始化生成器函数，返回生成器对象，简称生成器
gen = mygen()
#第一次无法给上一个yield发送数据，强制发送None 硬性的语法要求
res = gen.send(None)
print(res)

#第二次
res = gen.send(111)
print(res,'外头')

#第三次
res = gen.send(222)
print(res)

"""
# # 第四次 error   StopIteration
res = gen.send(333)
print(res,"<外头>")
"""

"""
代码执行过程:
第一次调用时,没有遇到上一个yield,所以默认只能发送None,执行生成器函数
print("start")  res1 = yield 1 记录当前代码执行的状态 把 1 
返回给函数外的res变量接受,程序添加阻塞,等待下一次调用 ,执行到91行

第二次调用时,把111发送给 	res1 = yield 1  , res1 = 111 接收到发送值,
代码从91往下执行 print(111) res2 = yield 2 把 2 返回给函数外的res变量接受	 print(res)		
程序添加阻塞,等待下一次调用 ,执行到94行							

第三次调用时,把222发送给   res2 = yield 2   , res2 = 222 接收到发送值,
代码从94往下执行 print(222) res2 = yield 3 把 3 返回给函数外的res变量接受	 print(res)
程序添加阻塞,等待下一次调用 ,执行到97行

第四次调用时,把333发送给   res3 = yield 3   , res3 = 333 接收到发送值,
代码从97往下执行 print(333) print("end") , 因为没有yield的返回值,直接越界报错.

解决生成器越界错误,可以使用try... except..方法解决.
"""
print('========')
#yield from  将一个可迭代对象变成一个迭代器返回
def mygen():
	yield from [1,2,3]

gen = mygen()
res = next(gen)
print(res)
res = next(gen)
print(res)
res = next(gen)
print(res)

print("<===>")

# 斐波那契数列 (用前两数相加得到第三个) (面试题)
# 1 1 2 3 5 8 13 21 34 .. 要第n个数是多少?

def mygen(n):
	a,b = 0, 1
	i = 0
	while i < n:
		yield b
		a,b = b, a+b
		i +=1
gen = mygen(5)
for i in gen:
	print(i)















































































