#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Сосчитать всех кто живет на улице Сукромка

from sukromka_street.house1 import room1
#~ ...

count = 0
inhabitants = room1.get_inhabitants()
count += len(inhabitants)


# и так далее для всех модулей в пакете street
....

print u'Всего живет ...'.format()

# ++ вывести полный список живущих на улице Сукромка
