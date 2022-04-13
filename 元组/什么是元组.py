#元组是python中内置的一种数据结构，是不可变序列
#常见的不可变序列有：元组、字符串，都没有增删改操作
#常见的可变序列有：列表、字典，可以对对象执行增删改操作，而且对象地址不发生改变

#可变序列：
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))    #改变前后地址不变

#不可变序列
s = "hello"
print(id(s))
s = s+"world"
print(id(s))     #改变前后地址发生改变
print(s)

#元组的创建格式
t = ("jack",1,2)   #和列表的区别是元组使用小括号()

