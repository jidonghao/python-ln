def print_triangle():
    for i in range(4):
        for j in range(0, 4 - i):
            print(" ", end="")
        for k in range(4 - i, 5):
            print("*", end=" ")

        print("")


print_triangle()
