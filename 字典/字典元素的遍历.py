scores = {"张三":100, "李四":200, "王五":300}
for item in scores:
    #item获取到的是键
    print(item,scores[item],scores.get(item))  #两种获取键对应的值的方法