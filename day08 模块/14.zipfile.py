# ### zipfile 压缩模块  后缀是zip
import zipfile

#[part1] 压缩文件
#1. 创建压缩包
zf = zipfile.ZipFile('ceshi01.zip', 'w',zipfile.ZIP_DEFLATED)

#写入文件
# write(路径,别名)
zf.write(r"D:\py_pro\基础\day08 模块\1.py", '111.py')

#可以在写入文件的同时，创建一个文件夹
zf.write(r"D:\py_pro\基础\day08 模块\1.py",'tmp/333.py')

#关闭文件
zf.close()

#[part2] 解压文件
zf = zipfile.ZipFile('ceshi01.zip', 'r')
"""
extractall   解压所有
extract      解压单个文件
"""

#解压所有文件到某个路径下， ./代表当前路径下的某个文件夹
# zf.extractall('./')
# zf.close()

#解压单个文件
zf.extract('111.py','./ceshi02')


#[part3] 追加文件，自动完成关闭zip压缩包操作
with zipfile.ZipFile('ceshi01.zip', 'a', zipfile.ZIP_DEFLATED) as zf:
	zf.write('5.py')

# [part4] 查看压缩包中的内容
with zipfile.ZipFile('ceshi01.zip', 'r', zipfile.ZIP_DEFLATED) as zf:
	lst = zf.namelist()

print(lst)








