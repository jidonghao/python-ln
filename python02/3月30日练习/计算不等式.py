# 计算 求到8
i = 1
sum = 0
while True:
    sum += 1 / i
    i += 1
    if sum >= 8:
        break
print(i-1)
