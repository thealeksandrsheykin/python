# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from controller import Main
from model import Phonebook

if __name__ == '__main__':
    with Phonebook('phonebook.db') as pb:
        while True:
            Main(pb).start()
