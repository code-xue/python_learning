#isidentifier:判断指定的字符是不是合法的标识符
s1 = "abc_"
print(s1.isidentifier())
print("张三abc".isidentifier())

#isspace:判断是否全部由空白字符组成
print("\t".isspace())

#isalpha:判断是否全部由字母组成
print("abc".isalpha())

#isdecimal:判断是否全部由十进制数字组成
print("123".isdecimal())

#isnumeric:判断是否全部由数字组成
print("123".isnumeric())

#isalnum:判断是否全部由字母和数字组成
print("abc123".isalnum())