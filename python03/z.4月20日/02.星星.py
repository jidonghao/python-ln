def print_triangle(n):
    for i in range(n + 1):
        for j in range(0, (n + 1) - i):
            print(end=" ")
        for k in range((n + 1) - i, (n + 1)):
            print("*", end=" ")

        print("")


print_triangle(4)
