#集合的判断操作
s1 = {100,200,300}
print(100 in s1)
print(400 in s1)

#集合元素的新增操作
#1.使用add()方法，一次只能新增一个元素
s1.add(400)
print(s1)

#2.使用update()方法，一次可以新增多个元素
s1.update({500,600,700})
print(s1)
s1.update([800,900])
print(s1)
s1.update((1000,))
print(s1)

#集合元素的删除操作
#1.使用remove()方法，一次删除一个指定元素，如果元素不存在则抛出keyerror
s1.remove(1000)
print(s1)
#s1.remove(2000)

#2.使用discard()方法，一次删除一个指定元素，如果元素不存在不抛异常

#3.调用pop方法，一次只删除一个任意元素,不能指定参数
s1.pop()
print(s1)

#4.使用clear()方法，清空集合
s1.clear()
print(s1)