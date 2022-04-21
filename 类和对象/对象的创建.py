#创建类的语法

class Student:    #采用驼峰命名法
    def __init__(self,name,age):
        self.name=name
        self.age=age

#示例方法
    def study(self):
        print("认真")
    def like(self):
        print("唱歌")

#静态方法
    @staticmethod
    def sm():
        print("静态方法")

#类方法
    @classmethod
    def cm(cls):
        print("类方法")

#对象的创建

stu1 = Student("张三",20)

print(id(stu1))
print(type(stu1))
print(stu1)

stu1.study()               #两种方法等价
Student.study(stu1)

print(stu1.name)
print(stu1.age)