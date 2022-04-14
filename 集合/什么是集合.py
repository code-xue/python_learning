#集合是python中内置的一种数据结构，与列表、字典一样都是可变序列
#集合是没有value的字典，也是无序的

#集合的创建方式
#1.直接用{}创建
s1 = {1,2,3,3,4,4,5,6}
print(s1,type(s1))   #集合中不存在相同元素，与key类似

#2.使用set()创建
s2 = set(range(6))
print(s2,type(s2))

#3.将列表中的元素转成集合
s3 = set([1,2,2,3,3,4,5])
print(s3,type(s3))

#4.将元组转成集合
s4 = set((1,2,3,4,5,65))
print(s4,type(s4))

#5.将字符串转成集合
s5 = set("python")
print(s5,type(s5))

#6.使用set()直接创建
s6 = set({1,2,3,5})
print(s6,type(s6))

#定义空集合:只能使用set()来定义
s7 = set()
print(s7,type(s7))
