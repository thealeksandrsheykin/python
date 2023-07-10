# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sqlite3
class Phonebook():
    def __init__(self):
        self.db = 'phonebook.db'
        connection = sqlite3.connect(self.db)
        with open(r'phonebook_schema.sql', 'r') as file:
            schema = file.read()
        connection.executescript(schema)
        connection.commit()
        connection.close()

    def _run_query(self, query, data = None):
        connection = sqlite3.connect(self.db)
        try:
            return connection.execute(query, )
        except sqlite3.IntegrityError as error:
            print(f'При выполнении запроса: {query} Возникла ошибка: {error}')
        connection.commit()
        connection.close()



    def add_new_contact(self):
        # query = 'insert into phonebook (full_name, phone_number, comment) values(?, ?, ?)'
        # data = {'full_name':    'ФИО (Иванов Иван Иванович)',
        #         'phone_number': 'номер ( +7 (123) 456-78-90 )',
        #         'comment':      'комментарий(Чтобы пропустить нажмите <Enter>)'}
        #
        # self._run_query()[input(f'Введите {data[key]}: ') for key in data]
        self._run_query('select * from phonebook;')







if __name__ == '__main__':
    pbook = Phonebook()
    pbook.add_new_contact()