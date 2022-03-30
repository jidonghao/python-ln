num = int(input("请输入要加的数字："))
n = int(input("相加的次数："))

temp = str(num)
sum = 0
while n:
    for i in range(1, n):
        temp += str(num)
    n -= 1
    sum += int(temp)
    temp = str(num)
print(sum)
