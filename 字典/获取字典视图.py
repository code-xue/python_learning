#1.获取字典中所有的键：用keys方法
scores = {"张三":100,"李四":200, "王五":300}
keys = scores.keys()
print(keys)
print(type(keys))  #keys是dict_keys类型
print(list(keys))  #将keys转化成列表

#2.获取字典中所有的值：用values方法
values = scores.values()
print(values)
print(type(values))
print(list(values))

#3.获取字典中所有的键值对：用items方法
items = scores.items()
print(items)
print(type(items))
print(list(items))  #列表中每个元素都是元组