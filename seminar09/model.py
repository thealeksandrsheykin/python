# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sqlite3
import text
import view


class Phonebook:

    def __init__(self, db: str) -> None:
        self.db = db

    def __enter__(self) -> callable:
        self.connection = sqlite3.connect(self.db)
        with open('phonebook_schema.sql', 'r') as file:
            schema = file.read()
            self.connection.executescript(schema)
            self.connection.commit()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.connection.close()

    def _run_query(self, query: str) -> callable:
        try:
            return self.connection.execute(query)
        except sqlite3.IntegrityError as error:
            print(f'При выполнении запроса: {query} Возникла ошибка: {error}')
        finally:
            self.connection.commit()

    def add_data(self) -> None:
        name, phone = view.show_input_data(text.user_input_data)
        self._run_query(f'insert into phonebook(name, phone) values ("{name}","{phone}");')

    def del_data(self) -> None:
        name, phone = view.show_input_data(text.user_input_data)
        self._run_query(f'delete from phonebook where name="{name}" and phone="{phone}"')

    def chg_data(self) -> None:
        selection = view.show_menu(text.change_menu)
        if selection == 1:
            name, phone = view.show_input_data(text.user_change_phone)
            self._run_query(f'update phonebook set phone = "{phone}" where name="{name}"')
        elif selection == 2:
            phone, name = view.show_input_data(text.user_change_name)
            self._run_query(f'update phonebook set name = "{name}" where phone="{phone}"')
        else:
            pass

    def srh_data(self) -> list:
        selection = view.show_menu(text.search_menu)
        if selection == 1:
            return self._run_query(f'select * from phonebook where phone="{input(text.user_search_phone)}"')
        elif selection == 2:
            return self._run_query(f'select * from phonebook where name="{input(text.user_search_name)}"')

    def shw_data(self) -> list:
        return list(self._run_query('select * from phonebook'))
