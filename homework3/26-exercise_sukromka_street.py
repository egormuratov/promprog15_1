#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Сосчитать всех кто живет на улице Сукромка

from sukromka_street.house1 import room1 as one, room2 as two
from sukromka_street.house2 import room1 as one2, room2 as two2


list = [one.get_inhabitants(), two.get_inhabitants(), one2.get_inhabitants(), two2.get_inhabitants()]

count = 0
inhabitants = one.get_inhabitants()
count = reduce(lambda a, b: a+b, [len(x) for x in list])



print u'Всего живет {N}'.format(N = count)

print (u'Список живущих на улице Сукромка: {all}'.format(all=', '.join([x for x in reduce(lambda x, y: x + y, list)])))
