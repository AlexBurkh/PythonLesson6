from random import randint

def print_equation(order : int, coefficients : list):
    line = f"k = {order} => "
    for i in range(k + 1)[::-1]:
        if i != k:
            line += "+ "
        if i == 0:
            line += f"{coefficients[i]} = 0"
            break
        line += f"{coefficients[i]} * x^{i} "
    print(line)

def generate_coefficients(k):
    coeficients = []
    for i in range(1, k + 2):
        coeficients.append(randint(0, 100))
    return coeficients

#k = input("Введите требуемую степень многочлена: ")
k = 3

print_equation(k, generate_coefficients(k))
