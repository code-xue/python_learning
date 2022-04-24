#1.__add__方法

a=1
b=2
c=a+b
d=a.__add__(b)    #加法其实是调用了a对象的__add__方法
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

stu1=Student("张三")
stu2=Student("李四")
s=stu1+stu2
print(s)        #通过改写add方法实现字符串相加

#2.__len__方法

lst=[1,2,3,4]
l=len(lst)
k=lst.__len__()   #len其实是调用了__len__方法
print(l)
print(k)

print(len(stu1))  #通过改写len方法实现计算stu1中name属性的长度

#3.__new__方法和__init__方法

class Person:
    def __new__(cls, *args, **kwargs):
        print("cls的id为%d" % id(cls))
        obj=super().__new__(cls)
        print("创建的对象的id为%d" % id(obj))
        return obj

    def __init__(self,name):
        print("self的id为%d" % id(self))
        self.name=name

print("object类的id为%d" % id(object))
print("Person类的id为%d" % id(Person))
x=Person("张三")
print("x的id为%d" % id(x))

