# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import text
import view
import sys
from tabulate import tabulate


class Main:
    def __init__(self, phonebook: str) -> None:
        self.pb = phonebook

    def start(self) -> None:
        selection = view.show_menu(text.main_menu)
        if selection == 1:
            self.pb.add_data()
        elif selection == 2:
            self.pb.del_data()
        elif selection == 3:
            self.pb.chg_data()
        elif selection == 4:
            print(tabulate(self.pb.srh_data()))
        elif selection == 5:
            print(tabulate(self.pb.shw_data()) if self.pb.shw_data() else text.empty_phone_book)
        elif selection == 6:
            sys.exit()

