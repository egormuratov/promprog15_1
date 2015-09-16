#! /usr/bin/env python
# -*- coding: utf-8 -*-

words = [u'Я', u'помню', u'чудное', u'мгновение', 
u'передо', u'мной', u'явилась', u'ты', ]

# выдать список длинн слов с помощью операции map
words_lengths = map(...)

# отфильтровать только длины слов, которые больше 4

def len_gt_4(param):
    return param > 4

filtered_words_lengths = filter(...)

# выдать сумму длин слов, длинна которых > 4

def summ(x, y):
    return x + y

total = reduce(...)
