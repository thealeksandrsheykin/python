# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import text


def show_menu(menu: list) -> int:
    for i, item in enumerate(menu):
        print(f'\t{i}. {item}' if i else f'{item}:')
    selection = input('Выберите пункт меню: ')
    while True:
        if selection.isdigit() and 0 < int(selection) <= len(menu) - 1:
            return int(selection)
        selection = input(text.menu_input_error.format(len(menu) - 1))


def show_input_data(data: list) -> list:
    print('Введите данные:')
    return [input(f'\t{i + 1}. {item}: ') for i, item in enumerate(data)]
