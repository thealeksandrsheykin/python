# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sqlite3
import sys

from tabulate import tabulate


class Phonebook:
    MENU1 = 'Выберите опцию:\n\t1.Изменить номер \n\t2.Изменить ФИО\n\t3.Добавить комментарий'
    MENU2 = 'Выберите опцию:\n\t1.Поиск по номеру\n\t2.Поиск по ФИО\n\t3.Поиск по комментарию'''

    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.connection = sqlite3.connect(self.db)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def _run_query(self, query):
        try:
            return self.connection.execute(query)
        except sqlite3.IntegrityError as error:
            print(f'При выполнении запроса: {query} Возникла ошибка: {error}')
        finally:
            self.connection.commit()

    def add_data(self):
        full_name = input('Введите ФИО(Иванов Иван Иванович): ')
        phone_number = input('Введите номер (+7 (123) 456-78-90): ')
        comment = input('Введите комментарий (Пропустить <Enter>): ')
        self._run_query(f'insert into phonebook(full_name, phone_number, comment) '
                        f'values ("{full_name}","{phone_number}","{comment}");')

    def del_data(self):
        full_name = input('Введите ФИО(Иванов Иван Иванович): ')
        phone_number = input('Введите номер (+7 (123) 456-78-90): ')
        self._run_query(f'delete from phonebook where full_name="{full_name}" and phone_number="{phone_number}"')

    def change_data(self):
        print(self.MENU1)
        selection = int(input('Введите опцию: '))
        if selection == 1:
            full_name = input('Введите ФИО для ка необходимо изменить номер(Иванов Иван Иванович):')
            phone_number = input('Введите новый номер (+7 123 456-78-90): ')
            self._run_query(f'update phonebook set phone_number = "{phone_number}" where full_name="{full_name}"')
        elif selection == 2:
            phone_number = input('Введите для какого номера необходимо поменять ФИО(+7 123 456-78-90): ')
            full_name = input('Введите новое ФИО(Иванов Иван Иванович): ')
            self._run_query(f'update phonebook set full_name = "{full_name}" where phone_number="{phone_number}"')
        elif selection == 3:
            phone_number = input('Введите для какого номера необходимо добавить комментарий(+7 123 456-78-90):')
            comment = input('Введите комментарий (Пропустить <Enter>): ')
            self._run_query(f'update phonebook set comment = "{comment}" where phone_number="{phone_number}"')
        else:
            return 0

    def search_data(self):
        print(self.MENU2)
        selection = int(input('Введите опцию: '))
        if selection == 1:
            phone_number = input('Введите номер (+7 123 456-78-90): ')
            print(tabulate(self._run_query(f'select * from phonebook where phone_number="{phone_number}"')))
        elif selection == 2:
            full_name = input('Введите ФИО(Иванов Иван Иванович): ')
            print(tabulate(self._run_query(f'select * from phonebook where full_name="{full_name}"')))
        elif selection == 3:
            comment = input('Введите комментарий: ')
            print(tabulate(self._run_query(f'select * from phonebook where comment="{comment}"')))
        else:
            return 0

    def show_all_data(self):
        print(tabulate(self._run_query('select * from phonebook')))


class Main():
    MENU = '''Выберите опцию\n\t1.Добавить контакт\n\t2.Удалить контакт\n\t3.Изменить контакт\n\t4.Найти контакт
    5.Показать все контакты\n\t6.Выйти'''

    def __init__(self, phonebook):
        self.phonebook = phonebook
        print(self.MENU)

        selection = int(input('Введите опцию: '))
        if selection == 1:
            self.phonebook.add_data()
        elif selection == 2:
            self.phonebook.del_data()
        elif selection == 3:
            self.phonebook.change_data()
        elif selection == 4:
            self.phonebook.search_data()
        elif selection == 5:
            self.phonebook.show_all_data()
        elif selection == 6:
            sys.exit()


with Phonebook('phonebook.db') as pb:
    while True:
        Main(pb)
