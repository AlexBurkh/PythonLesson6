# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
numbers = [2, 3, 45]
# # как бы я сделал на практике
# for number in numbers:
#     #print(str(bin(number))[2:]) # 10, 11, 101101 - красивый вывод
#     print(bin(number)) # 0b10, 0b11, 0b101101 - правильный вывод

# как скорее всего подразумевается в задании
def to_binary(number):
    binary = ''  
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary

for i in numbers:
    print(to_binary(i))
