# P26 2-3-5
n = int(input("输入一个正整数："))
s = ""
while n != 0:
    s += str(n % 10)
    n //= 10
print(s)
