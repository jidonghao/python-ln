ls = [5, 3, 8, 19, 11]
ls.sort()
print(ls)
ls.sort(reverse=True)
print(ls)
print("-----------")

lst = [5, 3, 8, 11, 4]
lst.reverse()
print(lst)
lst2 = [5, 3, 8, 11, 4]
print(lst2[::-1])

print("------3------")
ls1 = [4, 5, 2, 7]
ls2 = [3, 6]
lsA = ls1 + ls2
lsA.reverse()
print(lsA)

print("-----4-------")
ls4 = [1, 2, 5, 2, 9, 1, 3, 2, 1, 1]
print(ls4)
print("第一种")
print(list(set(ls4)))
print(ls4)
print("第二种方法")
forthLst = []
for i in ls4:
    if i not in forthLst:
        forthLst.append(i)
print(forthLst)
print("三：")
print(list(dict.fromkeys(ls4)))
ls4 = [1, 2, 5, 2, 9, 1, 3, 2, 1, 1]
print("四")
print(ls4)
a = 0
for i in range(0, len(ls4)):
    for j in range(i + 1, len(ls4)):
        if ls4[i] == ls4[j]:
            ls4.pop(j)
            break
print(ls4)
