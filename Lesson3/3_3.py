# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.1, 10.01] => 0.2

def count_max_def(list):
    fractionals = [round(item - int(item), 5) for item in list]
    return max(fractionals) - min(fractionals)

in_list = [1.1, 1.2, 3.1, 5, 10.01]
print(count_max_def(in_list))