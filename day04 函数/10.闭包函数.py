# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/25 22:48
"""
#闭包函数
'''
概念： 内函数使用了外函数的局变变量
并且外函数把内函数返回出来的过程，叫做闭包
这个内函数叫做闭包函数
'''
#1.基本语法：
def lizuqing_family():
	father = '李嘉诚'
	def father_say():
		print("{}说了:先定他一个小目标,买一个英国伦敦".format(father))
	return father_say
func = lizuqing_family()  #func = father_say
print(func)
func() #  father_say()

#2.闭包函数的升级
'''
内函数使用了 外函数的局部变量，外函数的局部变量与内函数发生绑定，延长了该变量的生命周期
'''
def liaopingping_family():
	jiejie = '马蓉'
	meimei = '马诺'
	money = 1000

	def jiejie_hobby():
		nonlocal money
		money -= 500
		print("买名牌包包,名牌手表,名牌狗链,.....家里的前还剩下%s"%(money))

	def meimei_hobby():
		nonlocal money
		money -= 400
		print("宁愿在宝马里面哭,也不愿再自行车上面撒欢.家里的钱还剩下%s"%(money))

	def big_guanjia():
		return jiejie_hobby, meimei_hobby  # 返回一个元组

	return big_guanjia

func = liaopingping_family()
print(func)
tup = func()
print(tup)

jiejie = tup[0]
jiejie()

meimei = tup[1]
meimei()