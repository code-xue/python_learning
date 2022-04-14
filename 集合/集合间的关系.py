#判断集合是否相等
s1 = {1,2,3,4}
s2 = {4,3,1,2}
print(s1==s2)   #与顺序无关
print(s1!=s2)

#一个集合是否是另一个集合的子集，使用issubset进行判断
s3 = {1,2,3,4,5,6,7,8,9}
s4 = {1,2,3,4}
s5 = {1,2,10}
print(s4.issubset(s3))
print(s5.issubset(s3))

#一个集合是否是另一个集合的超集，使用issuperset进行判断
print(s3.issuperset(s4))
print(s3.issuperset(s5))

#两个集合是否没有交集，使用disjoint进行判断
print(s3.isdisjoint(s4))  #False,说明有交集