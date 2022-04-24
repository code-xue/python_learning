#面向对象的三大特征：封装、继承、多态
#封装：提高程序的安全性
#     将属性和方法包装到类对象中，在方法内部对属性进行操作，在类对象的外部调用方法。
#     这样就无需关注方法内部的实现细节，从而隔离了复杂度
#     在python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，在前边加__

#继承：提高代码的复用性
#     如果一个类没有继承任何类，则默认继承object
#     python支持多继承
#     定义子类时，必须在其构造函数中调用父类的构造函数

#多态：提高代码的可拓展性和可维护性

#************************封装********************************
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def show(self):
#         print(self.name,self.__age)
#
# stu = Student("张三",20)
# stu.show()     #__age在类对象内部被使用，可以输出20
#
# #print(stu.__age)   #__age在类对象外部被使用，不能输出
#
# #print(dir(stu))
# print(stu._Student__age)    #通过这种方法也可以访问，但是谨慎使用


#*****************************继承**********************

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age,end=' ')

class Student(Person):
    def __init__(self,name,age,number):
        super().__init__(name,age)
        self.number=number
    def info(self):               #方法重写
        super().info()
        print(self.number)

class Teacher(Person):
    def __init__(self,name,age,yearofteacher):
        super().__init__(name,age)
        self.yearofteacher=yearofteacher
    def info(self):
        super().info()
        print(self.yearofteacher)


stu = Student("张三",20,123456)
teacher = Teacher("李四",40,10)
stu.info()
teacher.info()

#多继承
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass

#object类：是所有类的父类。所有类中都有object类中的方法
#不写继承时默认继承object类

#**************************************************多态******************************************
#就是“具有多种形态”，即使不知道一个变量所引用的对象是什么类型，仍然可以通过这个变量调用方法，
#在运行过程中根据变量所引用的对象的类型，动态决定调用哪个对象中的方法。

class Animal:
    def eat(self):
        print("动物吃肉")
class Dog(Animal):
    def eat(self):
        print("狗吃骨头")
class Cat(Animal):
    def eat(self):
        print("猫吃鱼")
class Person:
    def eat(self):
        print("人吃五谷杂粮")

def fun(obj):
    obj.eat()

fun(Animal())
fun(Dog())
fun(Cat())
fun(Person())

#pyhton是一门动态语言，崇尚“鸭子类型”，多态不要求继承关系，只看类中有无对应的方法。