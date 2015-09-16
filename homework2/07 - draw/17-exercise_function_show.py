#!/usr/bin/env python
# -*- coding: utf-8 -*-

# визуализировать функцию f(n) на плоскости c шагом 10
# вычислить остаток от целочисленного деления на 7 и отобразить цветом из набора
# 0 -> COLOR_DARK_RED
# 1 -> COLOR_DARK_ORANGE
# 2 -> COLOR_DARK_YELLOW
# 3 -> COLOR_DARK_GREEN
# 4 -> COLOR_DARK_CYAN
# 5 -> COLOR_DARK_BLUE
# 6 -> COLOR_DARK_PURPLE

# остаток от деления: 5 % 2 -> 1

from simple_draw import square, end, COLOR_DARK_PURPLE, Point


def f(x, y):
    return x / (y - 1)

for x in range(0, 600, 10):
    for y in range(0, 600, 10):
        z = f(x, y)
        color = ...
        square(left_bottom=Point(x, y), side=10, color=color)

# ++ попробовать другие функции x+y, x*y, x**2 + y**2, etc

# ++ с разным шагом

end()
