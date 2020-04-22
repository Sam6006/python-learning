# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/11 12:36
"""
import random

#计算器类
class Calc():
	def __init__(self, num,):
		self.num = num
	#加
	def __add__(self, other):
		print("%d + %d" %(self.num,other))
		return self.num + other
	#减
	def __sub__(self, other):
		print('%d-%d' %(self.num,other))
		return self.num - other
	#当附号在对象右边时执行此方法
	def __rsub__(self, other):
		print('%d-%d' % (other, self.num))
		return  other-self.num

rt = 0  # 正确次数
def result(ret,answer):
	"""
	#结果处理函数
	:param ret: 正确结果
	:param answer: 用户输入的结果
	:return:
	"""
	global rt
	if answer == ret:
		rt += 1
		return '回答正确，请继续答题'
	else:
		return '回答错误正确答案是：{}'.format(ret)

if __name__ == "__main__":
	print('张子宣同学,答题马上开始,请准备')
	i = 0
	while i < 10: #出题10次
		num1 = random.randint(1, 200)
		num2 = random.randint(1, 200)
		sign = random.choice(['+', '-'])
		obj = Calc(num1)  # 实例化对象
		if sign == '-':
			if num1 < num2:
				res1 = num2 - obj
			else:
				res1 = obj - num2
		else:
			res1 = obj + num2
		res2 = int(input('请输入你的运算结果:>>>>'))
		res = result(res1,res2)
		print(res)
		i += 1
	accuracy = rt/10
	print('张子宣同学本次共答对%d个,正确率为%.2f%%' % (rt, accuracy * 100))





