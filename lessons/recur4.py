def fib1(n):
    if n == 1 or n == 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)
n = int(input("Введите число="))
print(fib1(n))
