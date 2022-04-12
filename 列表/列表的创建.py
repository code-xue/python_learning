list1 = ["hello","world",98]
print(list1)
print(list1[0],list1[-3])
print(list1.index('hello'))
print(list1.index("hello",1,2))

list2 = [1,2,3,4,5,6,7,8,9]
print(list2[1:7:1])
print(list2[:7:1])
print(list2[::-1])
print(list2[8:0:-2])

print(1 in list2)
print(10 in list2)

for item in list2:
    print(item)