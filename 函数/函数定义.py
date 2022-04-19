#格式：def function():
#            return

#python可使用关键字传参，可根据形参名进行实参传递

def add(a,b):
    print(a)
    print(b)   #a=20,b=10
    c = a+b
    return c

ret = add(b=10,a=20)
print(ret)