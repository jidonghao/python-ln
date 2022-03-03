# P22 2-2-3
import math

print("求解一元二次方程的解：")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

if a == 0:
    print("不是一元二次方程")
else:
    d = b * b - 4 * a * c
    if d > 0:
        d = math.sqrt(d)  # 开方
        x1 = (-b + d) / 2 / a
        x2 = (-b - d) / 2 / a
        print("x1 = %f,x2 = %f" % (x1, x2))
    elif d == 0:
        print("x1=x2=",-b/2/a)
    else:
        print("无实数解")

