#python中可以给形参设置默认值，当实参与默认值不一致时取实参的值

def fun(a,b=10):
    print(a,b)

fun(100)
fun(20,30)

#个数可变的位置参数,结果为一个元组
def fun1(*args):
    print(args)

fun1(10)
fun1(10,20)

#个数可变的关键字参数，结果为一个字典
def fun2(**args):
    print(args)

fun2(a=10)
fun2(a=10,b=20)

#在一个函数的定义过程中，既有个数可变的位置参数，又有个数可变的关键字参数时，
#要求个数可变的位置参数在前，个数可变的关键字参数在后

#将列表、字典里面的元素作为实参
def fun3(a,b,c,d):
    print(a,b,c,d)

lst=[1,2,3,4]
fun3(*lst)

def fun4(a,b,c,d):
    print(a, b, c, d)

dict={"a":1,"b":2,"c":3,"d":4}
fun4(**dict)

#def fun5(a,b,*,c,d):  #c和d只能采用关键字实参传递