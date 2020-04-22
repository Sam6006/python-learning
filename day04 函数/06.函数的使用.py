# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/24 22:41
"""
#1.函数名的使用
#1.函数名是个特殊的变量，可以当做变量赋值

def func():
	print('函数名可以当成变量使用')

abc = 45
abc = func
print(abc)
abc()

#2.函数名可以作为容器类型数据的元素
def func1():
	print(1)
def func2():
	print(2)
def func3():
	print(3)
lst = [func1,func2,func3]
for i in lst:
	i()

#3 函数名可作为函数的参数
def func1(func):
	func()
def func2():
	print('woshi func2')

#func形参接收到func2这个实参函数，调用func1执行里面的代码块，调用func2()
func1(func2)

#4.函数名可以作为函数的返回值
def func3(func):
	return func

def func4():
	print('woshi func4')

#func4 这个实参func接收到，执行func3代码块内容，直接return func4, res 接收到了返回值func4
res = func3(func4)
print(res)
res()

# 2.__doc__或者help查看文档
# help(print)
res = print.__doc__
print(res)

#如何自定义函数的文档
def eat_big_chang(something):
	"""
	功能：模拟吃大肠的过程
	参数：大肠
	返回值： 吃没有吃完的状态
	"""
	print("我是在模拟{}过程".format(something))
	print("第一步.找肠子头")
	print("第二步.把肠子头放嘴里")
	print("第三步.使劲唆")
	return "擦擦嘴,满意的放下肠子.吃完了"

eat_big_chang('吃大肠')

#方法1 用函数.__doc__
res = eat_big_chang.__doc__
print(res)

#方法2
print('=====')
help(eat_big_chang)