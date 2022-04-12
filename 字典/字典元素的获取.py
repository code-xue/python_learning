#1.使用[]
scores = {"张三":100, "李四":200, "王五":300}
print(scores["张三"])
# print(scores["麻七"])

#2.使用get()
print(scores.get("张三"))

#两者区别是当要找的键不存在时，使用[]会报错keyerror
#使用get()不会报错，只会输出None，而且可以指定当找不到键时返回的值
print(scores.get("麻七"))
print(scores.get("陈六"),400)