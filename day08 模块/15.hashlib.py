# ### hashlib 模块
import hashlib
import random
#基本用法
#1.创建一个md5算法的对象
hs = hashlib.md5()
#2.把想要加密的字符串通过update 更新到hs对象中进行处理
hs.update('abc123'.encode('utf-8'))
#3.返回32位16进制的字符串
res = hs.hexdigest()
print(res,len(res))

# 加盐 (key 只有自己知道的关键字 ,目的就是增加密码的复杂度)
hs = hashlib.md5('xyz_'.encode('utf-8'))
hs.update('abc123'.encode('utf-8'))
res = hs.hexdigest()
print(res)

#动态加盐
res = str(random.randrange(10000,100000))
hs = hashlib.md5(res.encode('utf-8'))
hs.update('abc123'.encode('utf-8'))
res = hs.hexdigest()
print(res)

"""
# md5    加密效率快  , 安全性不是太高, 位数32位的16进制的字符串
# sha1   加密效率慢  , 安全性稍高, 更加精度 , 位数是40位的16进制字符串
# sha512 加密效率慢  , 安全性稍高, 更加精确 , 位数是128位的16进制字符串
"""
#sha算法系列
#hs = hashlib.sha1()
hs = hashlib.sha512()
hs.update('abc123'.encode())
res = hs.hexdigest()
print(res, len(res))

#hmac
'''
hmac 加密的字符串强度更高，不容易破解
'''
import hmac
key = b'abc'
msg = b'abc123'
hm = hmac.new(key,msg)
res = hm.hexdigest()
print(res,len(res))

# 随机返回长度为32位的二进制字节流
import os
key = os.urandom(32)
print(key, len(key))

hm = hmac.new(key,msg)
print(res)


