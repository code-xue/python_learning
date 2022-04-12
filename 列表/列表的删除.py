#remove:一次只删除一个元素
        # 有重复元素删除第一个
        # 不存在报错

list6 = [1,2,3,4,5,6,7,8,9]
list6.remove(5)
print(list6)

#pop:删除一个指定索引位置上的元素
#    指定索引不存在报错
#    不指定索引默认删除最后一个元素

list6.pop(2)
print(list6)
list6.pop()
print(list6)

#切片法：一次删除至少一个元素
# new_list = list6[1:3]  #会创建一个新的列表
# print(new_list)

list6[1:3] = []  #不创建新列表，真正意义上的删除
print(list6)

#clear:清空列表
list6.clear()
print(list6)

#del:删除整个列表
del list6