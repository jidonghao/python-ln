# P29 2-4-1
n = int(input("n="))

m = 2
while m < n:
    if n % m == 0:
        break
    m += 1
if m == n:
    print("%d是质数" % n)
else:
    print("%d不是质数" % n)
