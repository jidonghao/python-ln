s1 = "hello hello python python python"

print(s1.replace("python", "java", 2))  # 匹配的字符串 要替换的字符串 替换最大次数
print(id(s1))  # 获取地址值
print(id(s1.replace("python", "java", 3)))

print(s1)
lst = ["hello", "world", "python"]

print(','.join(lst))
print(lst)

print(s1.startswith("h"))
print(s1.endswith("h"))
