#字符串是不可变类型，不具备增删改等操作，切片将产生新的对象
#格式：str[start:end:step]

s = "hello,Python"
s1 = s[:5]
s2 = s[6:]
newstr = s1+"!"+s2
print(s1)
print(s2)
print(newstr)
s3 = s[::2]
print(s3)
s4 = s[::-1]
print(s4)