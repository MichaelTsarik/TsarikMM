# -- coding: utf-8 --

"""
5.2 Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
"""


def minimal_divisor(number):
    min_dev = 2
    while min_dev <= number:
        if number % min_dev == 0:
            return min_dev
        min_dev += 1


my_number = int(input("Введите целое число больше 1: "))

print('Наименьший делитель: ', minimal_divisor(my_number))
