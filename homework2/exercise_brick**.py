#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Заданы размеры А, В листа бумаги и x, y - размеры конверты
# Определить, поместится ли бумага в конверте



A, B = 8, 9
x, y = 10, 7
# 1
print("")
print ("Размеры конверта: x, y = 10, 7")
if A <= x and B <= y or A<= y and B <=x:
	print ("True! Лист бумаги меньше чем конверт")
else :
    print ("False! Лист бумаги больше чем конверт")

# 2
x, y = 10, 17
print("")
print ("Размеры конверта: x, y = 10, 17")
if A <= x and B <= y or A<= y and B <=x:
	print ("True! Лист бумаги меньше чем конверт")
else :
    print ("False! Лист бумаги больше чем конверт")


# (**усложненное) Заданы размеры А, В прямоугольного отверстия и размеры х, у, z кирпича. 
# Определить, пройдет ли кирпич через отверстие. 