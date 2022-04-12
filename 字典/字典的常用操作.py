#key是否存在的判断
scores = {"张三":100, "李四":200, "王五":300}
print("张三" in scores)
print("张三" not in scores)

#字典元素的删除
del scores["张三"]  #删除张三对应的键值对
print(scores)
#清空字典
# scores.clear()
# print(scores)

#添加元素
scores["陈六"] = 400
print(scores)

#元素的值的修改
scores["陈六"] = 500
print(scores)