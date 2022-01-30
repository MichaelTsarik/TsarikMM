# -- coding: utf-8 --

"""
4.3 Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, то длина
первой части должна быть на один символ больше). Переставьте эти две части местами, результат запишите в новую строку
и выведите на экран. Решение задачи должно быть выполнено без использования конструкции if и ей подобных.
"""


def string_reverse(string):
    str_size = len(string)
    i_left = (len(string) - len(string) // 2)

    left = string[:i_left]
    right = string[str_size - i_left:]

    new_string = right + left
    return new_string


my_string = 'VSUETBestEducation'
print('Исходная строка:\n' + my_string)

string_reverse(my_string)
print('\nИзмененная строка:\n' + string_reverse(my_string))
