#python中函数可以以元组的形式返回多个值

def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst = [1,2,3,4,5,6,7,8,9,10]
ret = fun(lst)
print(ret)