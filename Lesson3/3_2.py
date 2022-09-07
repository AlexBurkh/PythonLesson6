# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math

def count_mul(list):
    result_list = []
    max_index = math.ceil(len(list) / 2)

    for i in range(max_index):
        mul = list[i] * list[-i - 1]
        result_list.append(mul)

    return result_list

#in_list = [2, 3, 5, 6]
in_list = [2, 3, 4, 5, 6]

print(count_mul(in_list))
    