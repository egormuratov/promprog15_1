#! /usr/bin/env python
# -*- coding: utf-8 -*-

my_list = [2, 3, 5, 7, 9, 13, 21, 25, 38, 42, 65, 90, ]

# разделить на 3.0 те элементы
# которые делятся нацело на 5
# в результате должен получится укороченный список my_list_3
my_list_3 = []

# вариант 1 - c помощью цикла for
for x in my_list:
    if x%5 == 0:
        my_list_3.append(x/3.0)
print ('Вариант 1 ='), my_list_3


# вариант 2 - с помощью операций map и filter
def method(x):
    return x/3.0

print ('Вариант 2 = {i}'.format(i = list(map(method,filter(lambda x: x%5==0,my_list)))))

# # # вариант 3 - с помощью спискового выражения с условием
# [... if ...]
