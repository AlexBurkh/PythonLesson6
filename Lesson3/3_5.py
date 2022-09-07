# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def count_fibonacci(order):
    positive_fibonacci = []
    negotive_fibonacci = []

    for i in range(order + 1):
        if (i == 0):
            positive_fibonacci.append(0)
        elif (i == 1):
            positive_fibonacci.append(1)
            negotive_fibonacci.append(1)
        else:
            positive_fibonacci.append(positive_fibonacci[i - 2] + positive_fibonacci[i - 1])
            negotive_fibonacci.append((-1) ** (i + 1) * positive_fibonacci[i])
    
    return negotive_fibonacci[::-1] + positive_fibonacci

order = 8
print(count_fibonacci(order))
