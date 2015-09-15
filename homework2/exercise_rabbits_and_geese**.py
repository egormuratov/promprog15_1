#!/usr/bin/env python
# -*- coding: utf-8 -*-

# У гусей и кроликов вместе 64 лапы. Сколько может быть кроликов и гусей (указать все сочетания)? 
j = 0
i = 0
total_legs = 64
for rabbits in range(total_legs):
    for geese in range(total_legs):
        if rabbits*4 <= 64 and geese*2 <=64:
        	j+=1
        	if rabbits*4 + geese*2 == total_legs:
            		i+=1
print ('количество сочетаний:', i)
print ('количество переборов', j)
# оптимизировать количество переборов
