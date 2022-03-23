# 1
age = int(input("输入你的年龄："))
if age >= 18:
    print("恭喜你已成年！")
else:
    print("你还是小朋友！")

# 2
age = int(input("输入年龄："))
if 0 <= age <= 120:
    print("合法")
else:
    print("不合法")
# 3
python_score = float(input("输入成绩1："))
c_score = float(input("输入成绩2："))

if python_score > 60 or c_score > 60:
    print("合格")
else:
    print("不合格")

# 4
is_employee = True
if is_employee:
    print("允许入内")
else:
    print("不允许入内")
