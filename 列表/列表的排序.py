#sort:默认升序排序，加上参数reverse=True即为降序,而且不新建列表
list8 = [51,10,60,88,34,65]
list8.sort()
print(list8)
list8.sort(reverse=True)
print(list8)

#sorted:将排序后的元素放到一个新的列表里，注意和sort使用语法上的差别
list9 = [51,10,60,88,34,65]
new_list = sorted(list9)
print(new_list)
desc_list = sorted(list9,reverse=True)
print(desc_list)