# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/22 22:24
"""
#文件的相关函数

#把文件对象可以遍历 文件对象也是一个可迭代性数据
'''
fp = open("0322_1.txt",mode="r+",encoding="utf-8")
#readable()  功能：判断文件对象是否可读
res = fp.readable()
print(res)
#writable()	    功能: 判断文件对象是否可写
res = fp.writable()
print(res)

#文件对象可以遍历，默认遍历一次，读取一行
for i in fp:
	print(i)
	
'''

#readline 读取一行文件内容
'''
readline(字符个数)
如果参数字符个数大于当前行所有字符个数，那么读取一行
如果参数字符个数小于当前行所有字符个数，那么读取实际字符数
'''
with open('0322_1.txt', mode='r', encoding='utf-8') as fp:
	res = fp.readline(20)
	print(res)
	# res = fp.readline()
	# res = fp.readline()
	# print(res)
	# while res:
		# print(res)
		# res = fp.readline()

#readlines() 将文件中的内容按照换行读取到列表当中
lst_new = []
with open('0322_1.txt', mode='r', encoding='utf-8') as fp:
	lst = fp.readlines()
	print(lst)
	for i in lst:
		res = i.strip()
		lst_new.append(res)

print(lst_new)

#writelines()  将内容是字符串的可迭代性数据写入文件中，参数：为字符串类型的可迭代数据
'''
1.括号里的参数是可迭代性数据
2.内容的类型是字符串
'''
with open("0322_5.txt",mode="w",encoding="utf-8") as fp:
	lst = ['我爱你\n', '美丽的哈姆雷特\n', '我喜欢你潇洒的面庞\n', '修长的手指头\n', '和 文雅的气质\n', '那忧郁的眼神\n', '让我神魂颠倒不能自拔\n']
	fp.writelines(lst)

#truncate() 功能：把要截取的字符串提取出来，然后清空内容将提取的字符串重新写入文件中(字节)
with open("0322_5.txt",mode="r+",encoding="utf-8") as fp:
	fp.truncate(9)

'''
总结：
	read(字符)
	seek(字节)
	readline(字符)
	truncate(字节）
'''
