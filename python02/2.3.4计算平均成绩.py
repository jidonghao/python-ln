# P25 2-3-4
s = 0
i = 0
while i < 5:
    m = float(input("第" + str(i + 1) + "个成绩："))  # str() 将指定值转为字符串
    i += 1
    s += m
print("平均成绩为：", s / 5)
