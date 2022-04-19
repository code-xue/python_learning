#求n的阶乘

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

ret = fac(6)
print(ret)

#斐波那契数列

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
ret = fib(40)
print(ret)

for i in range(1,7):
    print(fib(i))