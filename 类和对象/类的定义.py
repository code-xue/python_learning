#创建类的语法

class Student:    #采用驼峰命名法
    name="张三"


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