# -- coding: utf-8 --

"""
3.7  По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи можно использовать только один
цикл. Пользоваться математической библиотекой math в этой задаче запрещено.
"""


def sum_factorials_calculation(number):
    number_factorial = 1
    total_sum = 1
    for i_num in range(2, number + 1):
        number_factorial *= i_num
        total_sum += number_factorial
    return total_sum


my_number = int(input('Введите число: '))

print(f'Сумма факториалов чисел от 1 до {my_number} равна: {sum_factorials_calculation(my_number)}')
