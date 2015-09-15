#!/usr/bin/env python
# -*- coding: utf-8 -*-

# нарисовать квадрат 5х5 пикселей в произвольном месте экрана

from simple_draw import rectangle, end, COLOR_DARK_GREEN, Point

color = COLOR_DARK_GREEN
left_bottom = Point(100, 100)
right_top = Point(150, 150)

rectangle(left_bottom, right_top, color)

end()

