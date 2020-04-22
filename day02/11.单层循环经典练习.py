# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/8 15:17
@Auth ： Sam
@File ：11.单层循环经典练习.py
@IDE ：PyCharm
"""

# 1.打印一行十个小星星
# help 查看函数的帮助文档
help(print)
# end="" 默认不换行,在最后一个字符的后面插入空字符取代\n
print("<===>")
"""
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
print("*",end="")
"""
i = 1
while i <=10:
	print("*",end='')
	i +=1
print("<===============>")
# 2.用变量拼接字符串的形式,打印一行十个小星星
i = 1
strvar = ''
while i <=10:
	strvar += "*"
	i +=1
print(strvar)

# (3)打印一行十个小星星 奇数个打印★ 偶数个打印☆
"""
0 % 2 = 0
1 % 2 = 1
2 % 2 = 0
3 % 2 = 1
4 % 2 = 0
...

0 % 3 = 0
1 % 3 = 1
2 % 3 = 2

3 % 3 = 0
4 % 3 = 1
6 % 3 = 2
...

0 % 8 = 0
1 % 8 = 1
2 % 8 = 2
3 % 8 = 3
4 % 8 = 4
5 % 8 = 5
6 % 8 = 6
7 % 8 = 7
8 % 8 = 0
.....
1.任意数和n取余 : 值得范围 0~(n-1)
"""
i = 1
while i < 11:
	# 所有的代码写在中间... 下面..

	# 输出星星的代码
	if i % 2 ==0:
		print("☆",end='')
	else:
		print("★",end='')

	i +=1
# (4)用 一个循环 打印十行十列小星星
print("<====>")
"""
**********
**********
**********
**********
**********
**********
**********
**********
**********
**********

# 如何打印100颗星星?
"""
i = 0
while i < 100:
	# 打印星星
	print("*",end='')
	if i % 10 == 9:
		# 打印换行 因为默认end="\n"
		print()
	i += 1
"""
规律:
0123456789  10111213141516171819   20212223242526272829
**********  * * ********           **********          **********************************************************************
            0 1 23456789           0123456789
"""

# (5)一个循环 打印十行十列隔列变色小星星(一个循环)
"""
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
"""

i = 0
while i <100:
	#打印星星
	if i % 2 ==0:
		print("☆",end='')
	else:
		print("★",end='')
	if i %10 == 9:
		print()
	i +=1
# (6)一个循环 打印十行十列隔行变色小星星(一个循环)
"""
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
"""
print('==========')
"""
0 // 3 = 0
1 // 3 = 0
2 // 3 = 0

3 // 3 = 1
4 // 3 = 1
5 // 3 = 1

6 // 3 = 2
7 // 3 = 2
8 // 3 = 2

0 // 4 = 0
1 // 4 = 0
2 // 4 = 0
3 // 4 = 0

4 // 4 = 1
5 // 4 = 1
6 // 4 = 1
7 // 4 = 1

8 // 4  = 2
9 // 4  = 2
10 // 4 = 2
11 // 4 = 2

12 // 4 = 3
....

2.任意数 和 n进行地板除,会出现n个相同的数字
3.地板除可以获取一个数的高位,取余可以获取一个数的低位
	89 // 10 = 8 (高位)
	89 % 10  = 9 (低位)
"""
i = 0
while i <100:
	#打印星星
	if i // 10 % 2 == 0:
		print("☆",end='')
	else:
		print("★",end='')
	if i % 10 == 9:
		#换行
		print()
	i +=1

"""
当i 范围在0~9   // 10 会出现10个相同的0  0在和2取余,余数是0
当i 范围在10~19 // 10 会出现10个相同的1  1在和2取余,余数是1
当i 范围在20~29 // 10 会出现10个相同的2  2在和2取余,余数是0
当i 范围在30~39 // 10 会出现10个相同的3  3在和2取余,余数是1
当i 范围在40~49 // 10 会出现10个相同的4  4在和2取余,余数是0
当i 范围在50~59 // 10 会出现10个相同的5  5在和2取余,余数是1
当i 范围在60~69 // 10 会出现10个相同的6  6在和2取余,余数是0
当i 范围在70~79 // 10 会出现10个相同的7  7在和2取余,余数是1
当i 范围在80~89 // 10 会出现10个相同的8  8在和2取余,余数是0
当i 范围在90~99 // 10 会出现10个相同的9  9在和2取余,余数是1
"""

