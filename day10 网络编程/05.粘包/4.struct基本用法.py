import struct

#pack 打包

'''
struct.pack 把任意长度的数字转化成具有固定长度的4个字节的值，组成字节流
pack('i', 2100000000) 代表我要转换的这个数据类型是整型，这个整型一般放的是字节长度
i = int

'''

#unpack 解包
'''
struct.unpack 把4个字节的值恢复成原有的数据，返回的是元组
'''

res = struct.pack('i', 10000)
#小于22亿的长度范围
res = struct.pack('i',2100000000)
print(res)
print(len(res))

#i 把二进制字节流转换成整型， unpack 返回的是元组， 通过下标0直接拿到数据
res = struct.unpack('i', res)[0]
print(res)