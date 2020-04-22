# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/22 16:59
"""
#文件操作

'''
对象.属性
对象.方法() 来调用其中的内容
fp = open(文件名，采用的模式，字符编码)
open 返回的是一个文件io对象，别名--文件句柄
i ===input 输入
o ===output 输出
'''

#文件写入操作
#打开文件
fp = open('ceshi0322.txt',mode='w',encoding='utf-8')
#写入内容
fp.write('abc')
#关闭文件
fp.close()

#文件读取操作
#打开文件
fp = open('ceshi0322.txt',mode='r',encoding='utf-8')
#读取文件
res = fp.read()
print(res)
#关闭文件
fp.close()

# (3) encode 和 decode
# 将字符串和字节流(Bytes流)类型进行转换 (参数写成转化的字符编码格式)
    #encode() 编码  将字符串转化为字节流(Bytes流)
    #decode() 解码  将Bytes流转化为字符串
# \xe9\xbb\x84\xe8\x8a\xb1\xe7\x9c\x9f\xe5\xb8\x85
# encode 将字符串转化为字节流
strvar = "黄花真帅"
res = strvar.encode("utf-8")
print(res)

# decode 将Bytes流转化为字符串
strvar2 = b'\xe9\xbb\x84'
res = strvar2.decode('utf-8')
print(res)

strvar = "我爱你王文"
print(strvar.encode("utf-8"))

#wb rb
'''如果模式当中有b，不要指定encoding编码集，否则报错'''

#把内容变成二进制字节流存储在文件中
fp = open('0322_1.txt',mode='wb')
strvar = '王铁男真硬'
res = strvar.encode('utf-8')
fp.write(res)
fp.close()

#把二进制字节流从文件中读出来转换成原来的格式decode
fp = open('0322_1.txt',mode='rb')
res = fp.read()
fp.close()
print(res)

res = res.decode("utf-8")
print(res)


#复制图片
'''
但凡是图片或者是音频或者是视频，本质上都是二进制字节流的文件
如果想要复制，先把内容通过二进制字节流模式读取出来，
然后再写入到另一个文件中
'''
#把文件读取出来
fp = open('集合.png',mode='rb')
res = fp.read()
fp.close()

#把文件内容写到另一个文件中
fp = open('集合2.png',mode='wb')
fp.write(res)
fp.close()


















