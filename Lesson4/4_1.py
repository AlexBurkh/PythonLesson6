def factorize(n : int):
    res = []
    i = 2
    while i <= int(n ** 0.5): # для положительных чисел округление int() аналогично math.floor()
        if not n % i:
            res.append(i)
            n = n / i
        else:
            i += 1
    res.append(n)
    return list(map(int, res))


n = input("Введите число для факторизации: ")
res = factorize(int(n))

print(res)