#1.直接使用()创建
t1 = ("python",80,90)
print(t1)
print(type(t1))
#也可以省略小括号
t3 = "prthon",80
print(t3)
print(type(t3))
#但是当元组中只有一个元素时后面还加上, 不然该元素的类型就是默认的类型
t4 = 90,
print(t4)
print(type(t4))

#2.使用内置函数tuple()
t2 = tuple(("python",80,90))
print(t2)
print(type(t2))


#空列表的创建方式
lst1 = []
lst2 = list()

#空字典的创建方式
dict1 = {}
dict2 = dict()

#空元组的创建方式
t5 = ()
t6 = tuple()