def max(*args):
    print(args)
    m = args[0]
    for i in range(len(args)):
        if m < args[i]:
            m = args[i]
    return m


print(max(1, 2, 5, 342, 234))
print(max(1))
