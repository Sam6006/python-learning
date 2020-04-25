# ### 计算一个文件夹所有文件的大小
import os

os.chdir("D:/py_pro/基础/") #切换目录
path1 = os.getcwd()  #获取目录

pathvar = os.path.join(path1,)
#
# print(pathvar)

# part1 基本操作
lst = os.listdir(pathvar)
print(lst)

# 初始化变量size =  0
size = 0
for i in lst:

	# 拼接成完整的绝对路径
	pathnew = os.path.join(pathvar, i)
	# 判定它是不是文件
	if os.path.isfile(pathnew):
		print(i, "是一个[文件]")
		# 如果是文件,计算大小 getsize 只能算文件的大小
		size += os.path.getsize(pathnew)
	# 判定它是不是文件夹
	elif os.path.isdir(pathnew):
		print(i, "是一个[文件夹]")
print(size)  # 4834


# part2 递归方法计算文件夹里所有内容大小
def getallsize(pathvar):
	size = 0
	lst = os.listdir(pathvar)

	for i in lst:
		pathnew = os.path.join(pathvar, i)
		if os.path.isfile(pathnew):
			print(pathnew)
			# 统计文件大小
			size += os.path.getsize(pathnew)
		elif os.path.isdir(pathnew):
			print(pathnew)
			# 递归统计文件夹里面的文件名称
			size += getallsize(pathnew)

	return size


res = getallsize(pathvar)
print(res)  # 6882 + 953 2048 4834





















