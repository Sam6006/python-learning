# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/8 16:18
@Auth ： Sam
@File ：01.pass break continue关键字.py
@IDE ：PyCharm
"""
# pass break continue

'''如果代码块当中，什么也不写，用pass 来进行占位'''
def func():
	pass

if 5 == 5:
	pass

#break 终止当前循环，只能在循环当中使用
#打印1-10 如果遇到5就终止循环
i = 1
while 1 < 10:
	print(i)
	if i == 5:
		break
	i +=1
# error
"""
if 5==5:
	break
"""
i = 1
while i<=3:
	j = 1
	while j<=3:
		if j == 2:
			print(i,j)
			break
		j+=1
	i+=1

#continue 跳过当前循环，从下一次循环开始  只能在循环中使用
#打印1-10  不包含5
'''
当i等于5时，continue跳过当前循环，后面的代码通通不执行
直接回到循环判断中，因为i没有自增，所以条件5<=10永远为真
发生死循环，为了 避免这个情况，所以我们手动加1，再执行continue.
'''
i = 1
while i <= 10:
	if i == 5:
		#手动自增，预防死循环
		i +=1
		continue
	print(i)
	i+=1
# 打印1~100 所有不包含4的数字.

# 方法一
print('====')
i = 1
while i <= 100:
	if i % 10 ==4 or i // 10 == 4:
		i +=1
		continue
	print(i)
	i +=  1

#方法二in
print('=====')
i = 1
while i <=100:
	num = str(i)
	if '4' in num:
		i+=1
		continue
	print(i)
	i+=1



