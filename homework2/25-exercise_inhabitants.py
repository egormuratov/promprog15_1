#!/usr/bin/env python
# -*- coding: utf-8 -*-

# вывести на консоль жителей комнаты 1 и 2 (модули room1 и room2)
# функция get_inhabitants возвращает список имен жителей
# Комната 1: Вася, Петя, Коля

from room1 import get_inhabitants

inhabitants = get_inhabitants()

# ','.join(['a', 'b', 'c', ]) => 'a,b,c'

names = ...
print u"В комнате 1 живут: ", names
print u"В комнате 1 живут: {names}".format(names=names)


#~ from ... import ...
#~ 
#~ print ... format ... join 
