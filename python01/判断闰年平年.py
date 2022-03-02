year = int(input("请输入年份："))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("%4d是闰年" % year)
else:
    print("%4d是平年" % year)
