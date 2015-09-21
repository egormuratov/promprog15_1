#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Даны пары однозачных чисел - кол-во забитых и кол-во пропущенных в футбольных играх
match_results = (
    (2,2),
    (2,1),
    (7,3),
    (0,0),
    (3,1),
    (0,5),
    (1,3),
    (5,3)
)

# Определить количество выйгрышей

wins, fail, draw, point = 0, 0, 0, 0
for x, y in match_results:
    if x > y:
        wins += 1
        point += 3
    elif x < y:
        fail +=1
        point += 1
    elif x == y:
        draw +=1

print u'всего выйгрышей:', wins
print u'всего проигрышей:', fail
print u'всего ничьих:', draw
print u'всего очков:', point

# Определить общее число очков, набранное командой
# выйгрыш +3 очка, ничья +1, проигрыш 0
