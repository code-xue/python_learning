#split:从字符串的左边开始劈分，默认劈分字符是空格，返回一个列表
s1 = "hello world python"
print(s1.split())
#也可以输入劈分参数，指定最大劈分次数
s2 = "hello|world|python"
print(s2.split("|"))
print(s2.split("|",1))

#rsplit:从字符串的右侧开始劈分，默认劈分字符是空格，返回一个列表
print(s1.rsplit())
print(s2.rsplit("|"))
print(s2.rsplit("|",1))