s1 = "hello hello python python python"

print(s1.replace("python", "java", 2))  # 匹配的字符串 要替换的字符串 替换最大次数
print(id(s1))  # 获取地址值
print(id(s1.replace("python", "java", 3)))

print(s1)
lst = ["hello", "world", "python"]

print(','.join(lst))  # 将列表转字符串
print(s1.split())  # 将字符串转列表
print(lst)

print(s1.startswith("h"))
print(s1.endswith("h"))

print("------------")

a = "hello"
b = "world"
c = "hello world"
print(a.upper())  # 不会改变原有序列
print(b.lower())
print(c.title())
print(c.capitalize())  # 首字母大写
print(c.swapcase())  # 全部大写 相当于upper
print(c.upper())

print(c.rjust(20, "-"))
print(c.center(20, "="))
print(c.ljust(20, "+"))
