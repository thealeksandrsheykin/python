# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Задача №1
Найдите сумму цифр трехзначного числа. Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
number = int(input('Введите трехзначное число: '))
input_number = number

first_number = number // 100
number = number % 100

second_number = number // 10
third_number = number % 10


print(f'{input_number} -> {first_number + second_number + third_number} ({first_number}+{second_number}+{third_number})')

"""
Задача №2
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый 
ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше 
журавликов, чем Петя и Сережа вместе? Пример:
6  -> 1   4   1
24 -> 4   16  4
60 -> 10  40  10
"""
s = int(input('Введите общее число журавликов: '))
intermediate_value = s // 3
print (f'{s} -> {intermediate_value // 2} {intermediate_value * 2} {intermediate_value // 2}')

"""
Задача №3
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет
с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
"""

ticket = input('Введите номер билета: ')
numbers_of_ticket = [int(i) for i in ticket]
if sum(numbers_of_ticket[:3]) == sum(numbers_of_ticket[3:]):
    print(f'{ticket} -> yes')
else:
    print(f'{ticket} -> no')

"""
Задача №4
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом 
по прямой между дольками (то есть разломить шоколадку на два прямоугольника).Пример:
3 2 4 -> yes
3 2 1 -> no
"""
n = int(input('Введите кол-во долек в ширину: '))
m = int(input('Введите кол-во долек в длину: '))
k = int(input('Введите кол-во долек, которые нужно отломить: '))

if k < (n * m) and (k % n == 0 or k % m == 0):
    print(f'{n} {m} {k} -> yes')
else:
    print(f'{n} {m} {k} -> no')
