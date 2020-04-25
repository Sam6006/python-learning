import sys
# sys.argv           命令行参数List，第一个元素是程序本身路径
# sys.exit(n)        退出程序，正常退出时exit(0),错误退出sys.exit(1)
# sys.version        获取Python解释程序的版本信息
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       返回操作系统平台名称

print(sys.argv)
# sys.exit()
# print(123)
#sys.argv 有什么用 怎么用
#返回值:列表  第一个元素是执行这个文件的时候，写在python命令后面的第一个值
#之后的元素 在执行python的启动的时候可以写多个值，都会被依次添加到列表中
# name = sys.argv[1]
# pwd = sys.argv[2]
# if name == 'alex' and pwd == 'alex3714':
# 	print('执行下面代码')
# else:
# 	exit()