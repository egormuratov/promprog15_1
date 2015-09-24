#!/usr/bin/env python
# -*- coding: utf-8 -*-

# нарисовать снежинку с помощью функции snowflake
from simple_draw import clear_screen, Point, snowflake, sleep, end, COLOR_ORANGE


class Snowflake:
    def __init__(self, x=100, y=500):  #начальные координаты
        self.coord_x = x
        self.coord_y = y

    def step(self, dx=0, dy=0): #шаг
        self.coord_x += dx
        self.coord_y += dy

    def draw(self): # рисуем снежинку
        point = Point(x=self.coord_x, y=self.coord_y)
        snowflake(center=point, color=COLOR_ORANGE)


snow = Snowflake() #с помощью этой переменной будем обращаться к методам класса

while True:
    clear_screen()
    snow.step(dy=-50)
    snow.draw()
    sleep(0.5)
    if snow.coord_y < 100:
        break

end()