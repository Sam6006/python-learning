import os

# os 和操作系统交互
#目录相关
# os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
# print(os.getcwd())
# 获取完整文件路径 5颗星
# print(__file__)
# os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
# os.chdir("D:/py_pro/基础/")
# print(os.getcwd())

#操作文件
# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
# os.mkdir('dir')

# os.makedirs('dirname1/dirname2')    可生成多层递归目录
# os.makedirs('dir2/dir3/', exist_ok = True)

# os.remove()  删除一个文件
# os.remove('dir2/dir3/aaa.py')
# os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.rmdir('dir')

# os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.removedirs('dir2/dir3/dir4')

# os.listdir('dirname') *****   列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# print(os.listdir("D:\py_pro\基础\day08 模块"))

# os.rename("oldname","newname")  重命名文件/目录

#查看文件信息
# os.stat('path/filename')  获取文件/目录信息
# res = os.stat(r'D:\py_pro\基础\day08 模块\01.模块.py')
# print(res.st_size)
"""
stat 结构:
st_mode: inode 保护模式
st_ino: inode 节点号。
st_dev: inode 驻留的设备。
st_nlink: inode 的链接数。
st_uid: 所有者的用户ID。
st_gid: 所有者的组ID。
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
st_atime: 上次访问的时间。
st_mtime: 最后一次修改的时间。
st_ctime: 由操作系统报告的"ctime"。
在某些系统上（如Unix）是最新的元数据更改的时间，
在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
"""
# os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# print(os.sep)
# os.linesep    输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
# print([os.linesep])
# os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
# print(os.pathsep)
# os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# print(os.name)

# os.system("bash command")  运行shell命令，直接显示
# os.system('dir')
# os.popen("bash command).read()  运行shell命令，获取执行结果
# ret = os.popen('dir').read()
# print(ret)


# os.path
# os.path.abspath(path) 返回path规范化的绝对路径
print(os.path.abspath(".")) #将相对路径转化为绝对路径

# os.path.split(path) 将path分割成目录和文件名二元组返回
print(os.path.split("D:/py_pro/基础/day08 模块/01.模块.py"))
print(os.path.split("D:/py_pro/基础/day08 模块"))

# os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.dirname("D:/py_pro/基础/day08 模块"))
print(os.path.dirname("D:/py_pro/基础/day08 模块/01.模块.py"))

# os.path.basename(path) 返回path文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.basename("D:/py_pro/基础/day08 模块/01.模块.py")) #01.模块.py
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
print(os.path.exists("D:/py_pro/基础/day08 模块/01.模块.py"))
# os.path.isabs(path)  如果path是绝对路径，返回True
print(os.path.isabs("D:/py_pro/基础/day08 模块/01.模块.py"))
# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile("D:/py_pro/基础/day08 模块"))
# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir("D:/py_pro/基础/day08 模块"))
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.join("D:/py_pro/基础/day08 模块/01.模块.py",'aaa','bbb'))


#splitext() 将路径分割为后缀和其他部分
pathvar = r"d:\周末四期\L006\filename.py"
res = os.path.splitext(pathvar)
print(res)

# os.path.getsize(path) 返回path的大小 5颗星
pathvar = r"D:/py_pro/基础/day08 模块/08.os模块.py"
res = os.path.getsize(pathvar)
print(res)

#islink()   检测路径是否是一个链接 (了解)
pathvar = r"D:\周末四期\L006\4.py"
res = os.path.islink(pathvar)
print(res)

# os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间

# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间


#getctime() [windows]文件的创建时间,[linux]权限的改动时间(返回时间戳)
pathvar = r"D:/py_pro/基础/day08 模块/08.os模块.py"
res = os.path.getctime(pathvar)
print(res)
import time
str_time = time.ctime(res)
print(str_time)

# getmtime() 获取文件最后一次修改时间(返回时间戳)
res = os.path.getmtime(pathvar)
print(res)
import time

str_time = time.ctime(res)
print(str_time)
# getatime() 获取文件最后一次访问时间(返回时间戳)
res = os.path.getatime(pathvar)
print(res)
import time

str_time = time.ctime(res)
print(str_time)



# isabs()    检测一个路径是否是绝对路径  abspath 4颗星
"""
别人传变量给你,先判断是不是绝对路径,如果不是用abspath配合转换.
"""
strvar = "."
res = os.path.isabs(strvar)
print(res)
