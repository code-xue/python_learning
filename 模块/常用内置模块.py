#sys:与Python解释器及其环境操作相关的标准库
#time:提供与时间相关的各种函数的标准库
#os:提供了访问操作系统服务功能的标准库
#calendar:提供与日期相关的函数的标准库
#urllib:用于读取来自网上（服务器）的数据标准库
#json:用于使用JSON序列化和反序列化对象
#re:用于在字符串中执行正则表达式匹配和置换
#math:提供标准算术运算函数的标准库
#decimal:用于进行精确控制运算精度、有效位数、和四舍五入操作的十进制运算
#logging:提供了灵活的记录事件、错误、警告、调试信息等日志信息的功能

# #sys
# import sys
# print(sys.getsizeof(10))    #获取对象在内存中的字节数
# print(sys.getsizeof(False))
#
# #time
# import time
# print(time.time())    #输出当前时间戳
# print(time.localtime(time.time()))

#urllib
import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())