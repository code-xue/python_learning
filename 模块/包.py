#包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下。
#作用：
#1.代码规范
#2.避免模块名称冲突
#包与目录的区别：包含__init__.py文件的称为包，没有就是目录

#包的导入：import 包名.模块名

import package.module_A as ma
print(ma.a)
#或者使用from 包名 import 模块名

#两种导入方式的区别
#import只能导入包名或者模块名
#from方式还可以导入变量
from package.module_A import a