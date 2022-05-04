lst = ["abc", "bcd", "cde"]
for i in lst:
    print(i)
print("-------")
for i in range(0, len(lst)):
    print(lst[i])

print("-----")
# 索引
lst = ["hello", "world", "77", "hello"]
# print(lst.index("python")
print(lst.index("hello", 1, 5))  # 在指定范围检索
print(lst[3])
print(lst[-3])

lst.insert(1, 90)
print(lst[1])

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(l[0:2])
print(l[:2])
print(l[:7:3])
print(l[2:-2])

print("------------")
name_list = ["张三", "李四", "王五"]
print("添加元素之前", name_list, id(name_list))
name_list.append("麻溜")
print("添加元素之后", name_list, id(name_list))

list2 = ["hello", "world"]
name_list.append(list2)
print("添加元素之后2", name_list, id(name_list))

name_list.append(list2)
print("添加元素之后3", name_list, id(name_list))

name_list.insert(1, 90)
print("添加元素之后4", name_list, id(name_list))

list3 = [True, False, "hello"]
name_list[1:] = list3
print(name_list)

