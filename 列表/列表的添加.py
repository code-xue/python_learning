#append:在列表的末尾添加一个元素，不会新建数组

list3 = [1,2,3,4,5]
list3.append(6)
print(list3)

#extend:在列表的末尾至少添加一个元素
list4 = [7,8]
list3.extend(list4)
print(list3)

#insert:在列表的任意位置添加一个元素

list3.insert(1,10)
print(list3)

#切片法：
list5 = [11,12,13,14,15]
list3[1:] = list5   #省略终止标志和步长
print(list3)