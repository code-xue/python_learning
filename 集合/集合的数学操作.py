#1.交集
s1 = {1,2,3,4,5,6}
s2 = {2,3,7,8}
print(s1.intersection(s2))
print(s1 & s2)
#.intersection()与&等价

#2.并集
print(s1.union(s2))
print(s1 | s2)
#.union()与|等价

#3.差集
print(s1.difference(s2))
print(s1 - s2)
#.difference()与-等价

#4.对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
#.symmetric_difference()与^等价