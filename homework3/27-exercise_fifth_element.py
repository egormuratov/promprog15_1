#!/usr/bin/env python
# -*- coding: utf-8 -*-

# умножение на пятый элемент
#
# возвести константу BRUCE_WILLIS в степень
# заданную цифрой в пятой позиции входной строки
#
# обработать исключительные ситуации 
# ValueError - невозможно преобразовать к числу
# IndexError - выход за границы списка

BRUCE_WILLIS = 42.0

input_data = raw_input('Enter elements:')

lilu = int(input_data[4])
result = BRUCE_WILLIS ** lilu
print u"Получилось {result}".format(result=result)


try:
    ...
except ValueError:
    ...
except IndexError:
    ...
else:
    ...



