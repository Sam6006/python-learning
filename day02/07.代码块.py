# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/7 18:07
@Auth ： Sam
@File ：07.代码块.py
@IDE ：PyCharm
"""

#代码块  以冒号作为开始 用缩进来划分作用域 这个整体是一个代码块
'''
作用域：作用的范围
看似距离相同，不代表是同一个缩进，比如4个空格和1个tab距离也是相同，但是并不是同一个代码块
1个tab的距离 = 4个空格，在写代码块的时，要么全用4个空格，要么全用1个tab缩进，不要混在一起作用
python 代码要比其他语言更加简洁，对代码的格式有要求
'''

print(11)
print(22)
print(33)


if 5 == 5:
	print(1)
	print(2)
	print(3)
    # print(4) # IndentationError
'''
if 6 != 6:
	print(5)
						print(6)
'''
# php 等其他语言用的是{}来包裹代码,表达同一个作用域
"""
# 了解
if(6==6){
	var_dump($a)
																																		var_dump($b)
}
"""

