#编码：将字符串转换成二进制数据
#解码：将二进制类型的数据转换成字符串类型

#编码
s = "中国矿业大学"
print(s.encode(encoding="GBK"))    #GBK一个汉字占两个字节
print(s.encode(encoding="UTF-8"))  #UTF-8一个汉字占三个字节

#解码
byte = s.encode(encoding="GBK")
print(byte.decode(encoding="GBK"))

byte = s.encode(encoding="UTF-8")
print(byte.decode(encoding="UTF-8"))