# -- coding: utf-8 --

"""
3.6  Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!. По данному натуральному n вычислите
 значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
"""


def number_factorial_calculation(number):
    number_factorial = 1
    for i_num in range(1, number + 1):
        number_factorial *= i_num
    return number_factorial


my_number = int(input('Введите число: '))

print(f'Факториал числа {my_number} равен {number_factorial_calculation(my_number)}')
