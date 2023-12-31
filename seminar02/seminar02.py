# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
№ Задача №1
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть. Пример:
5 -> 1 0 1 1 0
2
"""

arms = 0
tails = 0
number_of_coins = int(input('Введите кол-во монет: '))
side_of_coins = input(f'Введите как лежат {number_of_coins} монет (0-решка, 1 герб) через пробел: ')
array_of_coins = side_of_coins.split()

for i in range(number_of_coins):
    if array_of_coins[i] == '0':
        tails += 1
    else:
        arms += 1

print(f'{number_of_coins} -> {side_of_coins}')
print(tails)

"""
№ Задача №2
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два 
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму
этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.Пример:
4 4 -> 2 2
5 6 -> 2 3
"""

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

# Способ №1
# x + y = s
# x * y = p
# y = s - x => xs - x*x - p = 0
# D = (-s)**2 - 4 * p
# x = int((s + D ** 0.5)/2)
# y = int((s - D ** 0.5)/2)
# print(f'{s} {p} -> {x} {y}')

# Способ №2
for i in range(s):
    for j in range(p):
        if s == i + j and p == i * j:
            print(i, j)


"""
№ Задача №3
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
"""

number = int(input('Введите число N: '))

i = 0
print(f'{number} ->', end=' ')
while 2 ** i <= number:
    print(f'{2 ** i}', end=' ')
    i += 1
