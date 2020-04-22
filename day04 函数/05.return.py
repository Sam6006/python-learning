# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/24 22:29
"""
# return 函数的返回值，只出现在函数里
'''
return 自定义返回值，如果没有写return，默认返回None
功能：把值返回到函数的调用处
1.return 后面可以返回值，是自定义的，除了6大标准数据类型之外，还有类，对象，函数
2.如果执行了return 语句，意味着函数终止，后面的代码不执行
'''
#1 return 后面可以返回值，是自定义的，除了6大标准数据类型之外，还有类，对象，函数
def func():
	#return 1
	#return 3.14
	#return 3+4j
	#return True
	#return [1,2,3]
	return {"a":1,"b":2}
res = func() #res={'a':1,'b':2）
print(res)

#2 如果执行了return 语句，意味着函数终止，后面的代码不执行
def func():
	print('这句话执行了1')
	print('这句话执行了2')
	return 1
	print('这句话执行了3')
	print('这句话执行了4')

res = func()
print(res)

print('======')
def func():
	for i in range(5):
		if i == 3:
			return i
		print(i)

res = func()
print("<===>")

#3.计算器小例子
def calc(sign,num1,num2):
	if sign == "+":
		res = num1 + num2
	elif sign == "-":
		res = num1 - num2
	elif sign == "*":
		res = num1 * num2
	elif sign == "/":
		if num2 == 0:
			return "除数不能为0"
		res = num1 / num2
	return res

res = calc('+',1,1)
res = calc("-",-1,90)
res = calc("*",52,10)
res = calc("/",52,10)
res = calc("/",5200,10)
print(res)














