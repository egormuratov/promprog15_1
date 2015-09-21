#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# выдайте по запросу номер клетки, в которой сидит животное
# через функцию списка .index() : list.index(value)
# которая выбрасывает исключение ValueError если value нет в списке

ask = 'elephant'
# ask = 'bear'

# определите действия по подчистке - отпустите всех животных на волю

try:
    n = zoo.index(ask)
    print ('{animal} находиться в клетки под номером - {n}'.format(n=n, animal=ask))
except ValueError:
    print ('{animal} - Не найден в зоопарке'.format(animal=ask))