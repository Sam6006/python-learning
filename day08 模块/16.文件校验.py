# ### 文件校验
import hashlib

"""
read  在mode = "r"  读取的单位是字符
read  在mode = "rb" 读取的单位是字节;
"""
"""
with open("ceshi1.py",mode="r",encoding="utf-8") as fp:
	res = fp.read(3)
print(res)

with open("ceshi1.py",mode="rb") as fp:
	res = fp.read(3)
print(res)
print(res.decode())
"""
# (1) 针对于小文件的内容校验
def check_md5(file):
	with open(file, mode='rb') as fp:
		hs = hashlib.md5()
		hs.update(fp.read())
	return hs.hexdigest()

# 如果两个文件加密的32位字符串相同,就可以说明两个文件的内容是一样的
res1 = check_md5("ceshi.txt")
res2 = check_md5("ceshi.txt")
print(res1)
print(res2)


#针对于大文件的内容校验
hs = hashlib.md5()
hs.update("昨天晚上\n拉肚子了".encode())
res = hs.hexdigest()
print(res)

#可以利用update 分次更新内容
#利用update 这个特性，可以把较大的内容分次进行加密
hs = hashlib.md5()
hs.update("昨天晚上\n".encode())
hs.update("拉肚子了".encode())
res = hs.hexdigest()
print(res)

# 方法一 不停的读字节,直到为空的时候,终止循环
def check_md5(file):
	#创建对象
	hs = hashlib.md5()
	with open(file, mode='rb') as fp:
		while True:
			# 按照每次读取一个字节
			content = fp.read()
			#如果读取的是空字节，那么直接break
			if content:
				hs.update(content)
			else:
				break
		return hs.hexdigest()
print('========')
print(check_md5('1.py'))
print(check_md5('1.py'))

# 方法二 不停的减去响应的字节数,直到减到0,循环终止;
import os

#计算文件大小， os.path.getsize(文件名)
def check_md5(file):
	file_size = os.path.getsize(file)
	hs = hashlib.md5()
	with open(file, mode='rb') as fp:
		while file_size:
			content = fp.read(1)
			hs.update(content)
			file_size -= len(content)

		return hs.hexdigest()

print(check_md5('1.py'))
print(check_md5('1.py'))




















