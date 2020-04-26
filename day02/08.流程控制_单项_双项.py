# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/7 18:12
@File ：08.流程控制_单项_双项.py
@IDE ：PyCharm
"""

#流程控制
'''
流程：代码执行的过程
流程控制：就是对代码执行的过程进行管控

流程控制的三大结构
	顺序结构：代码块从上到下，依次执行
	分支结构：4小类
	循环结构: while for
分支结构：关键字  ifcao
	(1)单项分支
	(2)双项分支
	(3)多项分支
	(4)巢状分支
'''
# (1)单项分支
'''
语法：
	if 条件表达式
		code1
		...
	如果条件表大式成立，那就是返回真True,就会执行代码块
	如果条件表达式不成立，那就返回假False 不会执行代码块

'''
guoyimeng = "美女"
guoyimeng = "绿巨人"
if guoyimeng == "美女":
	print("给你买好吃的")
	print("给你买好喝的")
	print("给你买兰蔻")
	print("给你买倩碧")
	print("给你买香奈儿")
	print("给你买LV")
	print("给你买兰博基尼")
	print("给你买包,因为包治百病!")

# 双项分支: (2个当中选一个)
"""
if 条件表达式:
	code1
	code2..
else:
	code3
	code4...

如果条件表达式为真,那就是返回真True,执行code1和code2..
如果条件表达式为假,那就是返回假False,执行code3和code4..

if   下面的代码块也可以叫做真区间
else 下面的代码块也可以叫做假区间
"""
huanghua = '高富帅'
huanghua = "屌丝"
if huanghua == '高富帅':
	print("我就嫁给你")
else:
	print("你是个好人~")

"""
	模拟网站的登录
	等待用户输入账号和密码;
	账户是admin 密码是111
	如果条件满足,就让他登录
	如果条件不满足,就告诉他登陆失败
"""
# input 等待用户输入字符串 , 他返回的数据类型是字符串
# res = input("先森~,你妈贵姓~:")
# print(res,type(res))

username = input("请输入您的用户名:")
password = input("请输入您的密码:")

if username == 'admin' and password == '111':
	print("恭喜你~ 登陆成功")
else:
	print("抱歉,登录失败")























