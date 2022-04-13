#使用内置函数zip()生成字典
#zip:用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表

items = ["张三","李四","王五"]
prices = [70,80,90]
dict1 = {item:price    for item,price in zip(items,prices)}
print(dict1)