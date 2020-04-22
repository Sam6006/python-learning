# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/22 17:32
"""
# 文件的扩展模式
''' 在w, r, a 三个模式的后面套上一个+号，使该模式又可读，又可写'''
#read()  功能：读取字符的个数（里面的参数代表字符个数）
#seek()  功能：调整指针的位置（里面的参数代表字节个数）
	#seek(0)   移动到文件开头
	#seek(0,2) 移动到文件结尾
#tell()  功能：当前光标左侧所有的字节数 （返回字节数）


#r+   先读后写
# fp = open('0322_2.txt', mode='r+', encoding='utf-8')
# res = fp.read()
# print(res)
# fp.write('789')
# fp.close()

#r+ 先写后读
# fp = open('0322_2.txt',mode='r+', encoding='utf-8')
# # 把光标移动到最后,防止对原字符进行替换
# fp.seek(0,2)
# fp.write('999')
# fp.seek(0)
# res = fp.read()
# fp.close()
# print(res)

#w+ 可读可写
'''
fp = open('0322_3.txt', mode='w+', encoding='utf-8')
fp.write('666')
fp.seek(0)
res = fp.read()
fp.close()
print(res)
'''
#a+ 可读可写（当写入时，强制把光标移动到最后
#默认a模式可写
'''
fp = open('0322_4.txt', mode='a',encoding='utf-8')
fp.write('999')
# fp.read() error
fp.close()
'''

# (2)a+模式可读可写
'''
fp = open('0322_4.txt', mode='a+',encoding='utf-8')
fp.write('1234565')
fp.seek(0)
res = fp.read()
fp.close()
print(res)
'''

#追加内容时，光标是强制在最后的，如果是读取可以随意调整光标位置
"""
fp = open("0322_4.txt",mode="a+",encoding="utf-8")
fp.seek(0)
fp.write("123")
fp.close()

"""
#read seek tell综合使用
#read 后面加的参数值单位是字符个数，如果不写值，代表读取所有
'''
fp = open('0322_4.txt', mode='r+', encoding='utf-8')
fp.seek(3)
res = fp.read(2)
print(res)

# 获取当前光标左侧所有的字节数的
res = fp.tell()
print(res)
fp.close()
'''
#有中文的时候要小心，一个中文代表的是3个字节，在移动seek时，容易出现乱码
"""读中文字符如果不完整发生报错"""
"""
fp = open("0322_4.txt",mode="r+",encoding="utf-8")
fp.seek(3)
res = fp.read()
print(res)
"""
# print("我".encode()) #\xe6\x88\x91

#with 语法，可以自动实现关闭操作close()
# 把文件内容读出来
# fp = open("集合.png",mode="rb")
# res = fp.read()
# fp.close()

# 用with改写  as 就是起别名的意思  叫fp
with open('集合.png',mode='rb') as fp:
	res = fp.read()

# 把文件内容写到另外一个文件中
# fp = open("集合2.jpg",mode="wb")
# fp.write(res)
# fp.close()
with open('集合3.png',mode='wb') as fp:
	fp.write(res)

#简化操作
with open('集合.png',mode='rb') as fp1, open('集合4.png',mode='wb') as fp2:
	res = fp1.read()
	fp2.write(res)