# -- coding: utf-8 --

"""
4.9 Пользователь вводит строку и символ для удаления. Необходимо удалить этот символ из всей строки.
"""


def symbol_remove(string, symbol):
    new_string = string.replace(symbol, '')
    return new_string


my_string = input('Введите строку: ')
my_symbol = input('Введите символ для удаления: ')

print('\nИзмененная строка:\n' + symbol_remove(my_string, my_symbol))
