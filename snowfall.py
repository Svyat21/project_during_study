# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(-100, 600)
        self.y = sd.random_number(600, 1200)
        self.length = sd.random_number(10, 25)
        self.factor_a = sd.random_number(3, 7) / 10
        self.factor_b = sd.random_number(30, 70) / 100
        self.factor_c = sd.random_number(60, 120)

    def move(self):
        if self.x > 250:
            self.x += sd.random_number(-14, 12)
            self.y -= sd.random_number(4, 21)
        else:
            self.x += sd.random_number(-6, 18)
            self.y -= sd.random_number(4, 21)

    def draw(self, color=sd.COLOR_WHITE):
        point_snow = sd.get_point(self.x, self.y)
        sd.snowflake(
            center=point_snow,
            length=self.length,
            color=color,
            factor_a=self.factor_a,
            factor_b=self.factor_b,
            factor_c=self.factor_c
        )

    def can_fall(self):
        if self.y >= 0:
            return True

    def clear_previous_picture(self):
        point_snow = sd.get_point(self.x, self.y)
        sd.snowflake(
            center=point_snow,
            length=self.length,
            color=sd.background_color,
            factor_a=self.factor_a,
            factor_b=self.factor_b,
            factor_c=self.factor_c
        )


# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

def get_flakes(count=20):
    flakes_list = []
    for _ in range(count):
        obj_flake = Snowflake()
        flakes_list.append(obj_flake)
    return flakes_list


def get_fallen_flakes():
    fallen_count = 0
    for i, element in enumerate(flakes):
        if not element.can_fall():
            del flakes[i]
            fallen_count += 1
    return fallen_count


def append_flakes(count):
    for _ in range(count):
        obj_flake = Snowflake()
        flakes.append(obj_flake)


flakes = get_flakes(20)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# Зачёт!
