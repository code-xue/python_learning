# #列表的生成式
# lst = [i for i in range(10)]
# print(lst)
#
# #集合的生成式
# s = {i for i in range(10)}
# print(s)


#给定两个列表，以列表的形式分别输出两个列表的索引为奇数位的元素
def odd(lst):
    lst1 = [lst[i] for i in range(1,len(lst),2)]
    return lst1

a = [1,2,3,4,5]
b = [7,8,9,10,12,13]
print(odd(a))
print(odd(b))