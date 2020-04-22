# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/8 15:39
@Auth ： Sam
@File ：13.双层循环经典练习.py
@IDE ：PyCharm
"""
# ### 双层循环练习
# (1)打印十行十列小星星 (用两个循环)

# 打印一行十个小星星
# i = 0
# while i<10:
	# print("*",end="")
	# i+=1

# 针对于一行十个星星,循环10次即可
j = 0 # j来控制行数 一共10行
while j < 10:
	# 在这个地方写你自己的逻辑

	# 里层循环控制打印一行十个星星
	i = 0
	while i <10:
		print('*',end='')
		i+=1
	# 在打印完一行之后,打印换行;
	print()
	j +=1

print("<====>")
# (2)打印十行十列隔列换色小星星
j = 0 # j来控制行数 一共10行
while j < 10:
	# 在这个地方写你自己的逻辑

	# 里层循环控制打印一行十个星星
	i = 0
	while i<10:
		if i % 2 == 0:
			print("☆", end='')
		else:
			print("★", end='')
		i +=1
	# 在打印完一行之后,打印换行;
	print()
	j +=1

# (3)打印十行十列隔行换色小星星
"""
外层j动一次,里面i的循环动10次,
外层动的慢,内层动的快
i和j切换即可;
"""
j = 0
while j <10:
	#打印星星
	i = 0
	while i <10:
		if j % 2 == 0:
			print("☆",end='')
		else:
			print("★",end='')
		i +=1
	print()
	j +=1

# (4)99乘法表
# 方向一 正序
print('====')
i = 1
while i <= 9:
	j = 1
	while j <=i:
		print('%d*%d=%2d ' %(i,j,i*j), end='')
		j+=1
	print()
	i +=1

# 方向二 倒叙
print("<>=====")
i = 9
while i > 0:
	# print(i)
	# 内层循环,循环几次完全取决于i
	j = 1
	while j <= i:
		print("%d*%d=%2d " % (i, j, i * j), end="")
		j += 1

	# 打印换行
	print()
	i -= 1
# (5)100 ~ 999 找吉利数字 111 222 123 321 888 ...
"""
789 
百位:789 // 100  => 7
十位:789 // 10 % 10 => 8
个位:789 % 10  => 9
"""
i = 100
while i <= 999:
	baiwei = i // 100
	shiwei = i // 10 % 10
	gewei = i % 10
	# 三个相同的数字
	if shiwei == gewei and shiwei == baiwei:
		print(i)

	# 123 456 789
	if shiwei == gewei - 1 and shiwei == baiwei + 1:
		print(i)

	# 321 765 876
	if shiwei == gewei + 1 and shiwei == baiwei - 1:
		print(i)
	i += 1
