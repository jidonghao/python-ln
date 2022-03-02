a = 1
b = 2
c = 3
d = 0

print("1.", a > b and b > c or a + b > c)
print("2.", a - b < c or b > c and not c)
print("3.", not d or b > c + a or a)
print("4.", (d and b and c > d and a * b > c))
print("5.", not (a > b and c > d))
print("6.", a * b > c or b + c > d and not d)
print("7.", c + d <= b + d and d < c or 2 * b > c)
print("8.", d < b or c > a + b + d and b < c + a)
