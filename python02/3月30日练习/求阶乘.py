num = int(input("请输入一个数字: "))
result = 1

if num < 0:
    print("负数不管")
elif num == 0:
    print("0 的阶乘为 1")
else:
    temp = num
    while temp:
        result *= temp
        temp -= 1
    print("%d 的阶乘为 %d" % (num, result))
