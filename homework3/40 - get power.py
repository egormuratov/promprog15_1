#!/usr/bin/env python
# -*- coding: utf-8 -*-


# написать функцию - генератор функций возведения в степень

def get_power(n):
    def internal(x):
        return x**n
    return internal

power_5 = get_power(5)
print ('2 ** 5 = '), power_5(2)
# должен выдать 2 ** 5 = 32
