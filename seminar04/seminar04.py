# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import random

"""
Задача №1
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все
те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа.
    n - кол-во элементов первого множества.
    m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.Пример:
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""
def add_number_to_list(number):
    return [int(input('Введите число: ')) for _ in range(number)]


n = int(input('Введите кол-во первого множества: '))
m = int(input('Введите кол-во второго множества: '))

# list_n = [random.randint(0, 100) for i in range(n)]
# list_m = [random.randint(0, 100) for i in range(m)]

print('Первый список: ')
list_n = add_number_to_list(n)
print('Второй список: ')
list_m = add_number_to_list(m)

print(*sorted(list(set(list_n).intersection(set(list_m)))))


"""
Задача №2
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по 
окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.

Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
выросло Ai ягод.

В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и
нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает
ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки. Пример:
4 -> 1 2 3 4
9
"""
n = int(input('Введите кол-во кустов: '))
a = [random.randint(0, 5) for _ in range(n)]
# -> max = a[i-1] + a[i] + a[i+1]
max_ = 0

print(f'{n} ->', end=' ')
print(*a)
for i in range(n):
    if a[(i-1) % n] + a[i % n] + a[(i+1) % n] > max_:
        max_ = a[(i-1) % n] + a[i % n] + a[(i+1) % n]
print(max_)


