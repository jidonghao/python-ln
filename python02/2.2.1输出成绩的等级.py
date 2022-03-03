# P21 2-2-1
m = float(input("输入成绩："))
if m < 0 or m > 100:
    print("输入无效")
if 90 <= m:
    print("A")
elif 80 <= m:
    print("B")
elif 70 <= m:
    print("C")
elif 60 <= m:
    print("D")
else:
    print("E")
