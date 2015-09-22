#! /usr/bin/env python
# -*- coding: utf-8 -*-

words = [u'Я', u'помню', u'чудное', u'мгновение', 
u'передо', u'мной', u'явилась', u'ты', ]

# выдать список длинн слов с помощью операции map
words_lengths = (list(map(lambda word: len(word), words)))
print words_lengths


# отфильтровать только длины слов, которые больше 4

def len_gt_4(param):
    return len(param) > 4

filtered_words_lengths = filter(len_gt_4, words)

print ('Колличество слов, длина которых больше 4 символов = {j}'.format(j=len(filtered_words_lengths)))

# выдать сумму длин слов, длинна которых > 4

def summ(x, y):
    return x + y

total = reduce(summ, filtered_words_lengths)

print ('сумму длин слов, длинна которых > 4 = {i}'.format(i=len(total)))

