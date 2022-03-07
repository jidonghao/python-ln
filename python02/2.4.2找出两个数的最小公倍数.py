# P29 2-4-2
a = int(input("a="))
b = int(input("b="))
if a > b:
    c = a
else:
    c = b
m = a * b
while c <= m:
    if c % a == 0 and c % b == 0:
        break
    c += 1
print(c)
