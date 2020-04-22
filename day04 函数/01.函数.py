# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/23 22:40
"""
#函数
'''
1.函数的定义：
	功能（包裹一部分代码，实现某一个功能 达成某一个目的
2.函数特点：
	可以反复调用，提高代码的复用性，提高开发效率，便于维护管理
'''
#3. 函数的基本格式
'''
函数的定义处
def func():
	code1..
	code2...
	
函数的调用处
func()
'''

def func():
	print('今天是个好日子')

func()

#4.函数的命名
'''
函数的命名

字母数字下划线,首字符不能位数字
严格区分大小且,且不能使用关键字
函数命名有意义,且不能使用中文哦


驼峰命名法：
1.大驼峰命名法：每个单词的首字符大写（一般在类中起名用这样的方式，推荐）
	mycar => MyCar   busstop => BusStop myhouse => MyHouse
	youcanyouupnocannobb => YouCanYouUpNoCanNoBb
2.小驼峰命名法：除了第一个单词首字符不用大写之外，剩下首字符都大写
	mycar => myCar  myhouse=>myHouse
	mycar => my_car  myhouse => my_house (推荐)

'''
#函数的定义处
def cheng_fa_biao_99():
	for i in range(9,0,-1):
		for j in range(1,i+1):
			print("{:d}*{:d}={:2d} ".format(i,j,i*j), end='')
		#换行
		print()
# 函数的调用处
# cheng_fa_biao_99()
# cheng_fa_biao_99()
# cheng_fa_biao_99()
# cheng_fa_biao_99()
# cheng_fa_biao_99()
# cheng_fa_biao_99()
# cheng_fa_biao_99()
# cheng_fa_biao_99()
# cheng_fa_biao_99()
# cheng_fa_biao_99()

for i in range(10):
	cheng_fa_biao_99()































