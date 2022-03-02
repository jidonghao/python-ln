import math
s=float(input("输入一个数："))
if s>= 0:
    s=math.sqrt(s)
    print("平方根是：",s)
else:
    print("负数不能开平方")
print("The end")