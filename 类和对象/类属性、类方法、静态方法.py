
class Student:    #采用驼峰命名法

    school="中国矿业大学"
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

#类属性：类中方法外的变量称为类属性，被该类的所有对象共享
#类属性的使用方法
stu1 = Student("张三",20)
stu2 = Student("李四",30)
print(stu1.school)
Student.school = "清华大学"
print(stu1.school)
print(stu2.school)

#类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
Student.cm()


#静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
Student.sm()
