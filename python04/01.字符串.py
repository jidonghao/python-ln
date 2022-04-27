str1 = "hello world"
for char1 in str1:
    print(char1)

for i in range(0, len(str1)):
    print(str1[i])

# 字符串转大写
print(str1.upper())
# 字符串转小写
print(str1.lower())

# 字符串查找函数 索引从0开始
print(str1.find('ll'))
# 倒着查
print(str1.rfind("d"))

# index 查询，用法与find完全一致，注意如果查找的字符串不存在将会报错
# print(str1.index("z"))

# 判断是否以某个字符开头 区分大小写
print(str1.startswith("h"))
# 判断是否以某个字符结尾
print(str1.endswith("d"))

print("%-10x|" % 10)
print("%04d" % 5)
print("%0.3f" % 2.3)

# 字符串格式化
print("{1} {0} {1}".format("hello", "world"))

words = "design"
print("{:<10}".format(words))
print("{:>10}".format(words))
print("{:@^10}".format(words))
print("{:@^1}".format(words))
print("{0:,}".format(314159267))
print("{0:.5f}".format(3.1415926))
print("{:.5}".format("python"))
print("{0:10.5f}".format(3.1415926))
