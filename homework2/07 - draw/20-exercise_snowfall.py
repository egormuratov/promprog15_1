#!/usr/bin/env python
# -*- coding: utf-8 -*-

# нарисовать снегопад - 7 движужихся снежинок радиусом от 10 до 60 
# снежинки падают с высоты 500 пикселов со скоростью 30 пикселов за такт
# на расстоянии 100 пикселов друг от друга
import random
from simple_draw import clear_screen, Point, snowflake, sleep, end, COLOR_DARK_GREEN

# class Snowflake:
#     def __init__(self, x=random.randint(10, 100), y=500):
#         self.coord_x = x
#         self.coord_y = y
#
#     def step(self, dx=0, dy=0):
#         self.coord_x += dx
#         self.coord_y += dy
#
#     def draw(self):
#         point = Point(x=self.coord_x, y=self.coord_y)
#         snowflake(center=point, color=COLOR_DARK_GREEN, length=10 )
#
# snow = Snowflake()
#
#
# while True:
#     clear_screen()
#     snow.step(dy=random.randint(-50,-10))
#     for i in range(7):
#         snow.draw()
#         sleep(0.1)
#     if snow.coord_y < 100:
#             break
#
# end()


# y = 500
# for i in range(10):
#     clear_screen()
#     y = ...  # как изменяется y для всех снежинок
#     for i in range(7):
#         point = Point(...)
#         snowflake(point)
#     sleep(0.3)
#
# # + нарисовать снежинки разных радиусов, для этого хранить список радиусов
# radiuses = [30, 20, 40, 10, 50, 70, ]
#
# # + сделать скорость падения уникальной для каждой снежинки,
# # для этого хранить список координат Y и скоростей по Y
# coordinates = [...]
# velocity = [...]
#
# # ++ сделать реальный снегопад, что бы снежинки порхали из стороны в сторону
#
# end()


