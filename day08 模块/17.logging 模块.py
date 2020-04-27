#功能
	#1.日志格式的规范
	#2.操作的简化
	#3.日志的分级管理

#logging不能帮你做的事
	#自动生成你要打印的内容
#需要程序员自己在开发的时候定义好
	#在哪些地方需要打印，要打印的内容是什么，内容的级别

#logging模块的使用
	#普通配置型 简单的 可定制化差
	#对象配置型 复杂的 可定制化强

# 认识日志分级

# import logging
# logging.debug('debug message')      # 调试模式
# logging.info('info message')        # 基础信息
# logging.warning('warning message')  # 警告
# logging.error('error message')      # 错误
# logging.critical('critical message')# 严重错误

# import logging
#
# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug('debug message')      # 调试模式
# logging.info('info message')        # 基础信息
# logging.warning('warning message')  # 警告
# logging.error('error message')      # 错误
# logging.critical('critical message')# 严重错误

# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S')
# logging.debug('debug message')      # 调试模式
# logging.info('info message')        # 基础信息
# logging.warning('warning message')  # 警告
# logging.error('error message')      # 错误
# logging.critical('critical message')# 严重错误

#参数配置
"""
logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有：

filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。
datefmt：指定日期时间格式。
level：设置rootlogger（后边会讲解具体概念）的日志级别
stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
"""

# basicConfig
# 不能将一个log信息既输出到屏幕 又输出到文件

# logger对象的形式来操作日志文件

# 创建一个logger对象
# 创建一个文件管理操作符
# 创建一个屏幕管理操作符
# 创建一个日志输出的格式

# 文件管理操作符 绑定一个 格式
# 屏幕管理操作符 绑定一个 格式

# logger对象 绑定 文件管理操作符
# logger对象 绑定 屏幕管理操作符

import logging

#创建一个logger对象
logger = logging.getLogger()

#创建一个文件管理操作符
fh = logging.FileHandler('logger.log',encoding='utf-8')

#创建一个屏幕管理操作符
sh = logging.StreamHandler()

#创建一个日志输出格式
format1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#文件管理操作符 绑定一个  格式
fh.setFormatter(format1)

#屏幕管理操作符 绑定一个格式
sh.setFormatter(format1)

logger.setLevel(logging.DEBUG)

# logger对象 绑定 文件管理操作符
logger.addHandler(fh)
# logger对象 绑定 屏幕管理操作符
logger.addHandler(sh)

logger.debug('debug message')      # 调试模式
logger.info('我的信息')        # 基础信息
logger.warning('warning message')  # 警告
logger.error('error message')      # 错误
logger.critical('critical message')# 严重错误












