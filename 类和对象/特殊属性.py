class A:
    pass
class B:
    pass
class C(B,A):
    def __init__(self,name):
        self.name=name

x=C("张三")
print(x.__dict__)    #示例对象的属性字典
print(C.__dict__)

print(x.__class__)    #x所属的类
print(C.__bases__)    #C类的父类的元组
print(C.__base__)     #C类继承的第一个父类
print(C.__mro__)      #查看类的层次结构
print(A.__subclasses__())   #查看A的子类
