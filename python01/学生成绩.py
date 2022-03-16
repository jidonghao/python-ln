# 计算学生成绩
math = float(input("请输入数学成绩："))
chinese = float(input("请输入语文成绩："))
english = float(input("请输入英语成绩："))
s = math + chinese + english
print("总分是：%3.3f 平均：%2.3f" % (s, s / 3))
