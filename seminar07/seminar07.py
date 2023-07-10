# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
Задача №1
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.
е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе не-
сколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в
программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все
не в порядке.Пример:

пара-ра-рам рам-пам-папам па-ра-па-дам
Парам пам-пам
"""


def check_rhyme(phrase):
    list_word = phrase.lower().split()
    cnt_vowels = lambda word: sum(1 for i in word if i in 'аоиеёэыуюя')
    return len(set([cnt_vowels(i) for i in list_word])) == 1


rhyme = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print('Парам пам-пам' if check_rhyme(rhyme) else 'Пам парам')


"""
Задача №2
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента 
функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов 
таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
"""

from tabulate import tabulate


def print_operation_table(operation, num_rows=6, num_columns=6):
    return [[operation(i, j) for i in range(1, num_rows + 1)] for j in range(1, num_columns + 1)]


print(tabulate(print_operation_table(lambda x, y: x * y)))
