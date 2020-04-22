# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/8 15:06
@Auth ： Sam
@File ：09.多项分支.py
@IDE ：PyCharm
"""

# ### 多项分支
"""
if 条件表达式1:
	code1
	code2
elif 条件表达式2:
	code3
	code4...
elif 条件表达式3:
	code5
	code6...
else:
	code7 ...
如果条件表达式1满足,返回真,就执行对应代码块,如果条件表达式1不满足,代码往下执行
看一看条件表达式2 是否成立,如果成立,就执行对应代码块,如果条件表达式2不满足,代码往下执行
看一看条件表达式3 是否成立,如果成立,就执行对应代码块,如果条件表达式3不满足,直接执行else这个区间的代码块

elif 可以有多个,也可以没有
else 只能有一个,也可以没有

只有当所有条件都不满足的时候,才会执行else区间.
多项分支是多选1的结果.
"""
youqian = True
# 双项分支
if youqian == True:
	print("我就嫁给你")
else:
	print("你是个好人")

youqian = False
youfang = False
youche = False
youyanzhi = False
youtili = False

# 多项分支
print("<=============>")
if youqian == True:
	print("我就嫁给你1")
elif youfang == True:
	print("我就嫁给你2")
elif youche ==True:
	print("我就嫁给你3")
elif youyanzhi == True:
	print("我就嫁给你4")
elif youtili == True:
	print("我就嫁给你5")
else:
	print("你是个好人啊6")

# 巢状分支 (单项分支 双项分支 多项分支的互相嵌套)
youqian = True
youfang = True
youche = True
youyanzhi = True
youtili = True

if youqian == True:
	if youfang == True:
		if youche == True:
			if youyanzhi == True:
				if youtili == True:
					print("我就嫁给你")
				else:
					print("恭喜你,成为我的1号备胎.")
			else:
				print("恭喜你,成为我的2号备胎.")
		else:
			print("恭喜你,成为我的3号备胎.")
else:
	print("抱歉,前面就是2路汽车,一会好赶不上了呦")

#出题 height
#女生找对象
	# 男生在1米~1.5米之间 小强 你在哪里?
	# 男生在1.5~1.7米之间 没有安全感~
	# 男生 1.7~ 1.8米之间 帅哥 留个电话
	# 男生 1.8~2米之间 帅哥 你建议多一个女朋友吗

# height = 0.5
# 方法一.通用写法
"""
height = float(input("请输入您的身高:"))
if 1<=height and height<=1.5:
	print("小强 你在哪里?")
elif height>1.5 and height<=1.7:
	print("没有安全感~")
elif height>1.7 and height <=1.8:
	print("帅哥 留个电话")
elif height>1.8 and height <=2:
	print("帅哥 你建议多一个女朋友吗")
else:
	print("没有符合条件的选项")
"""
# 方法二.python特有方法 可以连续比较
height = float(input('请输入您的身高:'))
if 1 <= height <= 1.5:
	print('小强你在哪里？')
elif 1.5 < height <= 1.7:
	print('没有安全感')
elif 1.7< height <= 1.8:
	print('帅哥，留个电话呗')
elif 1.8 < height <= 2:
	print("帅哥 你建议多一个女朋友吗")
else:
	print("没有符合条件的选项")
















