#try...except:输出错误类型

try:
    a=int(input("请输入一个整数"))
    b=int(input("请输入一个整数"))
    ret = a / b
    print(ret)
except ZeroDivisionError:
    print("分母不能为0")

#多个except：按照先子类后父类的顺序，为了避免遗漏，可以在最后增加BaseException
try:
    a=int(input("请输入一个整数"))
    b=int(input("请输入一个整数"))
    ret = a / b
    print(ret)
except ZeroDivisionError:
    print("分母不能为0")
except ValueError:
    print("不能输入字符")
except BaseException:
    print("出错了")

#try..except...else结构：没有异常就执行else对应的内容：
try:
    a=int(input("请输入一个整数"))
    b=int(input("请输入一个整数"))
    ret = a / b
except ZeroDivisionError:
    print("分母不能为0")
except ValueError:
    print("不能输入字符")
except BaseException:
    print("出错了")
else:
    print(ret)

#try...except...else...finally:执行except或者else，最后都执行finally
try:
    a=int(input("请输入一个整数"))
    b=int(input("请输入一个整数"))
    ret = a / b
except ZeroDivisionError:
    print("分母不能为0")
except ValueError:
    print("不能输入字符")
except BaseException:
    print("出错了")
else:
    print(ret)
finally:
    print("程序结束")

