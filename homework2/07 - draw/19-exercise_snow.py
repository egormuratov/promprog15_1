#!/usr/bin/env python
# -*- coding: utf-8 -*-

# нарисовать снег - 1000 снежинок радиусом от 10 до 60 в произвольных местах экрана,
import random
from simple_draw import snowflake, end, Point

for i in range(1,1000):
    position = Point(x=random.randint(0,600), y=random.randint(0,600))
    snowflake(center=position, length=random.randint(10,60))

end()


