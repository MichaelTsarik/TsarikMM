# -- coding: utf-8 --

"""
2.4 Обувная фабрика собирается начать выпуск элитной модели ботинок. Дырочки для шнуровки будут расположены в два ряда,
расстояние между рядами равно a, а расстояние между дырочками в ряду b. Количество дырочек в каждом ряду равно N.
Шнуровка должна происходить элитным способом “наверх, по горизонтали в другой ряд, наверх, по горизонтали и т.д.”
(см. рисунок). Кроме того, чтобы шнурки можно было завязать элитным бантиком, длина свободного конца шнурка должна
быть l. Напишите функцию, которая получает на вход четыре натуральных числа a, b, l и N - именно в таком порядке -
и должна  вывести одно число - искомую длину шнурка.
"""


def lace_len(row, col, free_len, hole_count):
    my_len = (free_len * 2 + row * (2 * hole_count - 1) + col * (hole_count - 1))
    return my_len


a = int(input('Введите расстояние между рядами "a": '))
b = int(input('Введите расстояние между дырочками в ряду "b": '))
L = int(input('Введите длину свободного конца шнурка "l": '))
N = int(input('Введите количество дырочек "n": '))

print('Длина шнурка - ', lace_len(a, b, L, N))
