# 找出素数因数所有的
# {number} n
def findAllFactorAndPrimeNumber(n):
    findAllFactorAndPrimeNumber.flag = 0
    for i in range(1, n + 1):
        if n % i == 0:
            for j in range(1, i + 1):
                if i % j == 0:
                    findAllFactorAndPrimeNumber.flag += 1
            if not (findAllFactorAndPrimeNumber.flag > 2):
                findAllFactorAndPrimeNumber.flag = 0
                print(i, end=",")


findAllFactorAndPrimeNumber(12)
