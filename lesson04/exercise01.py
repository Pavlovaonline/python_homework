
# n = int(input("Введите число: "))
# def primes_div (n):
#     primes = []
#     for i in range(2, n):
#         if n % i == 0:
#             primes += [i]
#     return primes
# print(primes_div(n))

n = int(input("Введите число: "))
def primes_div (n):
    count_primes = 0
    primes = []
    for i in range(2, n, 1):
        if n % i == 0:
            for j in range(2, i, 1):
                if i % j == 0:
                    count_primes += 1
            if count_primes == 0 and i not in primes:
                primes.append(i)
            count_primes = 0
    if len(primes) < 1:
        return print(n, "простое число.")
    elif len(primes) > 0:
        return print(f"Простые множители числа {n}: {primes}")

primes_div(n)

