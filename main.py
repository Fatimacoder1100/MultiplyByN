

#2nd function
def fun2(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        return result
print(fun2(5))