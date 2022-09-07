# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def count_fibonacci(order):
    if order == 0:
        return [0]
    if order == 1:
        return [1, 0, 1]
    elif order > 1:
        positive_fibonacci = [0, 1]
        negotive_fibonacci = []
        [positive_fibonacci.append(positive_fibonacci[i - 2] + positive_fibonacci[i - 1]) for i in range(2, order + 1)]
        [negotive_fibonacci.append((-1) ** (i + 1) * positive_fibonacci[i]) for i in range(1, len(positive_fibonacci))]
        return negotive_fibonacci[::-1] + positive_fibonacci

order = 7
print(count_fibonacci(order))
