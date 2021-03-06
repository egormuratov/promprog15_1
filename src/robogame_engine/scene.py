#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Pipe, Process
from random import randint
import time

from robogame_engine.events import EventCollide
from robogame_engine.geometry import Vector, Point
from robogame_engine.objects import ObjectStatus, GameObject
from robogame_engine.theme import theme
from robogame_engine.user_interface import UserInterface
from robogame_engine.utils import CanLogging


class Scene(CanLogging):
    """
        Game scene. Container for all game objects.
    """
    check_collisions = True
    _teams = {}

    def __init__(self, name='RoboGame', field=None, theme_mod_path=None, speed=None, **kwargs):
        theme.set_theme_module(mod_path=theme_mod_path)
        self.objects = []
        self._max_speed = self.get_max_speed(speed)
        GameObject.link_to_scene(
            scene=self,
            container=self.objects,
            max_speed=self._max_speed,
        )
        self.hold_state = False  # режим пошаговой отладки
        self.name = name
        if field:
            theme.FIELD_WIDTH, theme.FIELD_HEIGHT = field
        self.parent_conn = None
        self.ui = None
        self._step = 0
        self._checked_ids = []
        self.prepare(**kwargs)

    @staticmethod
    def get_max_speed(speed):
        if speed is None or speed > theme.NEAR_RADIUS:
            speed = theme.NEAR_RADIUS
        return speed

    def get_team(self, cls):
        try:
            return self._teams[cls.__name__]
        except KeyError:
            team = max(self._teams.values()) + 1 if self._teams else 1
            if team > theme.TEAMS_COUNT:
                raise Exception(
                    "Only {} teams! No team for {}".format(
                        theme.TEAMS_COUNT, cls.__name__))
            self._teams[cls.__name__] = team
            return team

    def prepare(self, **kwargs):
        raise NotImplementedError()

    def remove_object(self, obj):
        try:
            self.objects.remove(obj)
        except ValueError:
            self.logger.warning("Try to remove unexists obj {}".format(obj))

    def get_objects_by_type(self, cls):
        return [obj for obj in self.objects if isinstance(obj, cls)]

    def game_step(self):
        """
            Proceed objects states, collision detection, hits
            and radars discovering
        """
        self._checked_ids = []
        for obj in self.objects:
            obj.proceed_events()
            obj.proceed_commands()
            obj.game_step()
            if self.check_collisions:
                self._check_collisions(obj)
            self._checked_ids.append(obj.id)

    def _check_collisions(self, left):
        for right in self.objects:
            if (right.id == left.id) or (right.id in self._checked_ids):
                continue
            distance = left.distance_to(right)
            overlap_distance = int(left.radius + right.radius - distance)
            if overlap_distance > 1:
                # may intersect by one pixel
                module = overlap_distance // 2
                if right.coord.near(left.coord):
                    step_back_vector = Vector.from_direction(direction=randint(0, 360), module=module)
                else:
                    step_back_vector = Vector.from_points(right.coord, left.coord, module=module)
                left.debug('step_back_vector {}'.format(step_back_vector))
                left.coord += step_back_vector
                right.coord -= step_back_vector
                left.add_event(EventCollide(right))
                right.add_event(EventCollide(left))

    def get_objects_status(self):
        """

        """
        return dict([(obj.id, ObjectStatus(obj)) for obj in self.objects])

    def go(self):
        """
            Main game cycle - the game begin!
        """
        self.parent_conn, child_conn = Pipe()
        self.ui = Process(target=start_ui, args=(self.name, child_conn,))
        self.ui.start()

        while True:
            cycle_begin = time.time()

            # проверяем, есть ли новое состояние UI на том конце трубы
            ui_state = None
            while self.parent_conn.poll(0):
                # состояний м.б. много, оставляем только последнее
                ui_state = self.parent_conn.recv()

            # состояние UI изменилось - отрабатываем
            if ui_state:
                if ui_state.the_end:
                    break

                for obj in self.objects:
                    obj._selected = obj.id in ui_state.selected_ids

                # переключение режима отладки
                if ui_state.switch_debug:
                    if theme.DEBUG:  # были в режиме отладки
                        self.hold_state = False
                    else:
                        self.hold_state = True
                    theme.DEBUG = not theme.DEBUG

            # шаг игры, если надо
            if not self.hold_state or (ui_state and ui_state.one_step):
                self._step += 1
                self.game_step()
                # отсылаем новое состояние обьектов в UI
                objects_status = self.get_objects_status()
                self.parent_conn.send(objects_status)

            # вычисляем остаток времени на сон
            cycle_time = time.time() - cycle_begin
            cycle_time_rest = theme.GAME_STEP_MIN_TIME - cycle_time
            if cycle_time_rest > 0:
                # о! есть время поспать... :)
                time.sleep(cycle_time_rest)

        # ждем пока потомки помрут
        self.ui.join()

        print 'Thank for playing with robogame! See you in the future :)'


def start_ui(name, child_conn):
    ui = UserInterface(name, theme)
    ui.run(child_conn)


def random_point():
    x = randint(0, theme.FIELD_WIDTH)
    y = randint(0, theme.FIELD_HEIGHT)
    return Point(x, y)
