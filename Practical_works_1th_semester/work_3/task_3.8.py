# -- coding: utf-8 --

"""
3.8  По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без
пробелов.
"""


def stairs_building(size):
    for row in range(1, size + 1):
        for col in range(1, row + 1):
            print(col, end='')
        print()


steps_count = int(input('Введите количество ступенек: '))
stairs_building(steps_count)
