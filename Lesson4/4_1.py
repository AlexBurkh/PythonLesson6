def factorize(n : int):
    res = []
    i = 2

    while i * i <= n: # для положительных чисел округление int() аналогично math.floor()
        if not n % i:
            res.append(i)
            n = n // i
        else:
            i += 1
    res.append(n)
    return res


n = input("Введите число для факторизации: ")
res = factorize(int(n))

print(res)