class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def study(self):
        print(self.name+"学习很认真")

stu1 = Student("张三", 20)
stu2 = Student("李四", 30)
stu1.study()

#动态绑定属性
stu1.gender="男"
print(stu1.gender)
#print(stu2.gender)  #stu2中没有gender属性，报错

#动态绑定方法
def show():
    print("定义在类之外的，称为函数")
stu1.show=show   #将show函数动态绑定到stu1的方法中
stu1.show()
stu2.show()   #stu2中没有show方法，报错

