# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math


def count_max_def(list):
    fractionals = []
    for item in list:
        fractionals.append(round(item - int(item), 5))
    max_item = max(fractionals)
    min_item = min(fractionals)
    return max_item - min_item


in_list = [1.1, 1.2, 3.1, 5.4, 10.01, 5.9]

print(count_max_def(in_list))