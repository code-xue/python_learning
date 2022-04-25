#os模块是Python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关，
#在不同的操作系统上运行，得到的结果可能不一样
#os模块与os.path模块可用于对目录或文件进行操作

import os
os.system("notepad.exe")  #打开记事本
#os.startfile("")          #打开应用程序

#getcwd:返回当前的工作目录
#listdir:返回值定路径下的文件和目录信息
#mkdir:创建目录
#makedirs:创建多级目录
#rmdir:删除目录
#removedirs:删除多级目录
#chdir:将path设置为当前工作目录
