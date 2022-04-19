#1.使用%
name = "张三"
age = 20
print("我的名字叫%s,年龄%d岁" % (name,age))

#2.使用format
print("我的名字叫{0},年龄{1}岁".format(name,age))

#3.使用f-string
print(f"我的名字叫{name},年龄{age}岁")


#精度和宽度的设置
#1.使用%
print("%d" % 100)
print("%10d" % 100)
print("%10.3f" % 3.141592653)

#2.使用format
print("{0:10d}".format(100))
print("{0:10.3f}".format(3.141592653))