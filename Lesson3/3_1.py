# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def count_odd(list):
    sum = 0
    for i in range(len(list)):
        if not i % 2:
            sum += list[i]
    return sum

in_list = [2, 3, 5, 9, 3]

result = count_odd(in_list)
print(result)