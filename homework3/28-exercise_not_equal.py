#!/usr/bin/env python
# -*- coding: utf-8 -*-

# напишите функцию, которая будет порождать исключение NotEqual,
# если её параметры не равны

class NotEqual(Exception):
    pass


def is_equal(param1, param2):
    ...


# обработайте это исключение при вызове функции
# напишите "числа равны" или "числа неравны"

a = 27
b = 42

try:
    is_equal(...)
except NotEqual:
    ...
else:
    ...
