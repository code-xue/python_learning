#upper:将字符串中所有字符全部转成大写字母
#lower:将字符串中所有字符全部转成小写字母
s1 = "python"
s2 = s1.upper()
print(s2)
s3 = s2.lower()
print(s3)

#swapcase:将字符串中小写转成大写，将大写转成小写
s4 = "hello,Python"
print(s4.swapcase())

#capitalize:将第一个字母转成大写，其他转成小写
print(s4.capitalize())

#title:把每个单词的首字母转成大写，每个单词的剩余字符转成小写
print(s4.title())