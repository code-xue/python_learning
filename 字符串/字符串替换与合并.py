#replace:第一个参数指定倍替换的字符串，第二个参数指定用来替换的字符串
#返回替换后的字符串，替换前的字符串不发生变化，第三个参数指定最大替换次数
s1 = "hello,python"
print(s1.replace("python","java"))
s2 = "hello,python,python,python"
print(s2.replace("python","java",2))

#join:将列表或元组中的字符串合并成一个字符串
s3 = ["python", "hello","world"]
print("*".join(s3))
print("".join(s3))
print("*".join("python"))  #将字符串看成一个字符序列