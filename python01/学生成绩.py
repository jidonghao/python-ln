#计算学生成绩
math = float(input("请输入数学成绩："))
chinese = float(input("请输入语文成绩："))
english = float(input("请输入英语成绩："))
sum = math + chinese + english
print("总分是：%3.2f 平均：%2.2f"%(sum,sum/3))