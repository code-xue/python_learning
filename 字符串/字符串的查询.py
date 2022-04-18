#index方法和find方法
#index():查找子串第一次出现的位置，找不到报错
#rindex()：查找子串最后一次出现的位置，找不到报错
#find()：查找子串第一次出现的位置，找不到返回-1
#rfind()：查找子串最后一次出现的位置，找不到返回-1

s = "hello,hello,hello"
print(s.index("el"))
print(s.find("el"))
print(s.rindex("el"))
print(s.rfind("el"))
#print(s.index("abc"))
print(s.find("abc"))
#print(s.rindex("abc"))
print(s.rfind("abc"))