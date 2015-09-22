#! /usr/bin/env python
# -*- coding: utf-8 -*-

my_list = [2, 3, 5, 7, 9, 13, 21, 27, 42, 99, ]

# разделить каждый элемент списка на 3.0
# в результате должен получится список my_list_2
my_list_2 = []

# вариант 1 - c помощью цикла for 
for x in my_list:
    my_list_2.append(x/3.0)
print ('вариант 1 - c помощью цикла for, my_list_2 ='), my_list_2

# вариант 2 - с помощью операции map
print ('Вариант 2 - с помощью операции map, my_list_2 = {i}'.format(i = list(map(lambda x: x/3.0, my_list))))
#
# вариант 3 - с помощью спискового выражения
print ('Вариант 3 - с помощью спискового выражения, my_list_2 = {i}'.format(i = [x/3.0 for x in my_list]))

