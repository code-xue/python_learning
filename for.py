# sum = 0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
# print("和为：",sum)

#***********************输出100-999之间的水仙花数****************************
for i in range(100,1000):
    tmp = i
    sum = 0
    while tmp:
        n = tmp % 10
        sum = sum + n**3
        tmp //= 10
    if sum == i:
        print(i)