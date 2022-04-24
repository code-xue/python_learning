#import + 模块名
import math
print(math.pi)
print(math.pow(2,3))
print(math.ceil(9.001))
print(math.floor(9.999))

#form 模块名 import 方法名
from math import pi
print(pi)

#自定义模块的导入
#1.在目录右键->将目标记录为->源 根
import test
print(test.add(1,2))
#2.from 模块名 import 方法名