# -- coding: utf-8 --

"""
1.7 Проверьте является ли значение в переменной number - четным.
"""


def chek_number(number):
    if number % 2 == 0:
        print('Это число четное!')
    else:
        print('Число не четное.')


my_number = int(input('Введите число: '))
chek_number(my_number)
