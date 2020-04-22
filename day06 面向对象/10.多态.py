# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/6 16:38
"""
# ### 多态
"""

不同的子类对象,调用相同的父类方法,产生不同的执行结果
继承,重写
好处:多态针对的是对象来说的.在不改变原有代码的前提下,完成不同的功能;
不同的对象,调用相同的方法,达到了不同的功能.
"""
class Soldier():
	def attact(self):
		pass
	def back(self):
		pass

class Army(Soldier):
	def attact(self):
		print("[陆军]拿一把枪,突突突,然后倒下")
	def back(self):
		print("[陆军]撒腿就跑,躺下装死")

class Navy(Soldier):
	def attact(self):
		print("[海军]开炮,鱼雷,拿鱼叉子插死敌人")
	def back(self):
		print("[海军]立即跳海,下海喂鱼")

class AirForce(Soldier):
	def attact(self):
		print("[空军]空对地导弹,使用二营长的意大利跑射死别人")
	def back(self):
		print("[空军]立即跳伞,落地成盒")

# 实例化一个陆军士兵
obj_army = Army()
# 实例化一个海军士兵
obj_navy = Navy()
# 实例化一个空军士兵
obj_airforce=AirForce()

# 各就位准备
lst = [obj_army,obj_navy,obj_airforce]

# 将军请下令
strvar = '''
1.全体出击
2.全体撤退
3.空军上,其他人撤退
'''

while True:
	print(strvar)
	num = input("请将军下令>>>")
	if num.isdecimal():
		if int(num) == 1:
			for i in lst:
				i.attact()
		elif int(num) == 2:
			for i in lst:
				i.back()
		elif int(num) == 3:
			for i in lst:
				# 通过判断对象的类型,执行对应的方法
				if isinstance(i,AirForce):
					i.attact()
				else:
					i.back()
		else:
			print("风太大,我听不见!")
	else:
		if num.upper() == "Q":
			print("欢迎下次在指挥")
			break
