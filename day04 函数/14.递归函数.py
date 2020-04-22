# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/26 23:24
"""
#递归函数
'''
递归函数：自已调用自己的函数
递：去
归：回
一去一回是递归

递归的最大深度，官网说法是1000层  但实际是996- 1000
'''
#简单递归
def digui(n):
	print(n,'==1==')
	if n > 0:
		digui(n-1)
	print(n,'==2==')
digui(5)
"""
去的过程:
	n = 5
	print(5,"<==11==>")
	5 > 0 digui(5 - 1) digui(4)

	n = 4
	print(4,"<==11==>")
	4 > 0 digui(4 - 1) digui(3)

	n = 3
	print(3,"<==11==>")
	3 > 0 digui(3 - 1) digui(2)

	n = 2
	print(2,"<==11==>")
	2 > 0 digui(2 - 1) digui(1)

	n = 1
	print(1,"<==11==>")
	1 > 0 digui(1 - 1) digui(0)

	n = 0
	print(0,"<==11==>")
	0 > 0  条件不满足,往下执行
	print(0,"<==22==>")

回的过程: (把剩下的没走玩的代码继续执行)
	回到上一次函数的调用处第17行,从17行继续向下执行
	n = 1 print(1,"<==22==>")

	回到上一次函数的调用处第17行,从17行继续向下执行
	n = 2 print(2,"<==22==>")

	回到上一次函数的调用处第17行,从17行继续向下执行
	n = 3 print(3,"<==22==>")

	回到上一次函数的调用处第17行,从17行继续向下执行
	n = 4 print(4,"<==22==>")

	回到上一次函数的调用处第17行,从17行继续向下执行
	n = 5 print(5,"<==22==>")

	递归函数彻底终止.
"""
# 递归的最大深度 error
'''
def func():
	func() #[Previous line repeated 995 more times]
func()
'''

#栈帧空间:是为了运行函数所需要开辟的空间
'''
1.没调用一次函数，就是开辟一个栈帧空间的过程
每结束一次函数，就是释放一个栈帧空间的过程
递归函数就是不停的开辟栈帧空间和释放栈帧空间的过程

2.回的过程有两种触发时机
	1，当最后一层函数全部执行完毕，触发回的过程，回到上一层函数调用处
	2.当遇到return 返回值的时候，触发回的过程，回到上一层函数调用处
	
3.如果递归层数过大，不推荐使用递归，如果使用，务心添加一个跳出的条件，防止内存溢出
'''

#栈帧空间彼此的数据是隔离的，彼此独立，各是各的空间
def func(n):
	print(n)

func(1)
func(2)
# 计算n的阶乘 5! = 5*4*3*2*1
def jiecheng(n):
	if n <=1:
		return 1
	return n * jiecheng(n-1)
res = jiecheng(5)
print(res)

'''
5 * jiecheng(4)

4* jiecheng(3)
3 * jiecheng(2)
2* jiecheng(1)
1
需要先把表达式的值算完之后,再返回

# 去的过程
n = 5 return 5 * jiecheng(5 - 1) => 5 * jiecheng(4)
n = 4 return 4 * jiecheng(4 - 1) => 4 * jiecheng(3)
n = 3 return 3 * jiecheng(3 - 1) => 3 * jiecheng(2)
n = 2 return 2 * jiecheng(2 - 1) => 2 * jiecheng(1)
n = 1 n <= 1 满足 return 1

# 回的过程
n = 2 return 2 * jiecheng(2 - 1) => 2 * jiecheng(1) => 2 * 1
n = 3 return 3 * jiecheng(3 - 1) => 3 * jiecheng(2) => 3 * 2 * 1
n = 4 return 4 * jiecheng(4 - 1) => 4 * jiecheng(3) => 4 * 3 * 2 * 1
n = 5 return 5 * jiecheng(5 - 1) => 5 * jiecheng(4) => 5 * 4 * 3 * 2 * 1
最后直接 return  5 * 4 * 3 * 2 * 1 = 120




'''