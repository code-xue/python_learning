#**************************************************************************************************

#字典由键值对组成，键值对的排列是无序的，但3.6版本以后key变为有序，每个键通过哈希函数获得一个相应的位置，且无法被更改，所以键是不可变序列
#但是可以通过键修改其对应的值，所以字典是可变序列

#字典的创建

#1.使用{}创建字典
scores = {"张三":100,"李四":200,"王五":300}
print(scores)
print(type(scores))

#2.使用dict()创建
student = dict(name = "jack", age = 20)
print(student)

#3.创建空字典
d = {}
print(d)