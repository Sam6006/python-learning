# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/30 20:47
"""
#time 时间模块
import time
# 时间戳时间,格林威治时间,float数据类型  给机器用的
    # 英国伦敦的时间  1970.1.1 0:0:0
    # 北京时间 1970.1.1 8:0:0
    # 1533693120.3467407
# 结构化时间,时间对象                   上下两种格式的中间状态
    # 时间对象 能够通过.属性名来获取对象中的值
# 格式化时间,字符串时间,str数据类型      给人看的
    # 可以根据你需要的格式 来显示时间

#time() 获取本地时间戳  给机器看的
res = time.time()
print(res)

#mktime()  通过[时间元组]获取[时间戳] (参数是时间元组)
#年 月 日 时分秒, 周几， 年中第几天  夏令时
ttp = (2020,3,30,20,50,0,0,0,0)
res = time.mktime(ttp)
print(res)

#localtime()  通过[时间戳]获取[时间元组] 默认当前时间  结构化时间
#用法1
res = time.localtime()
print(res)
#time.struct_time(tm_year=2020, tm_mon=3, tm_mday=30, tm_hour=20, tm_min=52, tm_sec=23, tm_wday=0, tm_yday=90, tm_isdst=0)

#用法2 可以具体指定时间戳
res = time.localtime(1563704880)
print(res)

#ctime() 通过[时间戳] 获取[时间字符串]  默认当前时间 给人看的
res = time.ctime()
print(res) #Mon Mar 30 21:26:55 2020

res = time.ctime(1563704880)
print(res)

#asctime() 通过[时间元组] 获取[时间字符串] 参数是时间元组
'''asctime 不能够自动识别周几，需要手动填写'''
ttp = (2019,7,21,18,28,0,6,0,0)
res = time.asctime(ttp)
print(res)

#strftime() 通过[时间元组] 获取格式化时间字符串  (格式化字符串,[可选时间元组参数])
res = time.strftime('%Y-%m-%d %H:%M:%S')
print(res) #2020-03-30 21:31:11
# 加上第二个参数,按照实际的时间元组转成时间字符串,如果不加,以当前默认时间进行转化.
ttp = (2019,7,21,18,28,0,0,0,0)
res = time.strftime("%Y-%m-%d %H:%M:%S",ttp)
print(res)

#strptime() 通过时间字符串 获取 时间元组
strvar1 = "2019年8月1号5点10分20秒是建军节"
strvar2 = "%Y年%m月%d号%H点%M分%S秒是建军节"
res = time.strptime(strvar1,strvar2)
print(res)

#sleep() 程序睡眠等待
time.sleep(3)
print('ok 了')

#perf_counter()  用于计算程序运行的时间
starttime = time.perf_counter()
for i in range(1000000000):
	pass

endtime = time.perf_counter()
res = endtime - starttime
print(res)