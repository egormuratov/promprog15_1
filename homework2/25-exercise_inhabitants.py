#!/usr/bin/env python
# -*- coding: utf-8 -*-

# вывести на консоль жителей комнаты 1 и 2 (модули room1 и room2)
# функция get_inhabitants возвращает список имен жителей
# Комната 1: Вася, Петя, Коля

from room1 import get_inhabitants
from room2 import get_inhabitants2

inhabitants = get_inhabitants()
inhabitants2 = get_inhabitants2()

print u"В комнате 1 живут: {names}".format(names = ', '.join(inhabitants))
print u"В комнате 2 живут: {names}".format(names = ', '.join(inhabitants2))
