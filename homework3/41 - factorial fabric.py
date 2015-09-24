#!/usr/bin/env python
# -*- coding: utf-8 -*-


# написать генератор для получения последовательных факториалов

def factorial(N):
    value = 1
    for i in range(1, N+1):
        value *= i
        yield value
            
for f in factorial(5):
    print f
# должен выдать 1, 2, 6, 24, 120
