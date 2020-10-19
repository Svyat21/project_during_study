# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

start_point = sd.get_point(300, 30)


# def draw_branches(start_point, angle, len):
#     v1 = sd.get_vector(start_point=start_point, angle=angle + 30, length=len)
#     v1.draw(width=2, color=sd.COLOR_PURPLE)
#     v2 = sd.get_vector(start_point=start_point, angle=angle - 30, length=len)
#     v2.draw(width=2, color=sd.COLOR_PURPLE)

# draw_branches(start_point, 90, 150)

# def draw_branches(start_point, angle, len, width=10, color=sd.COLOR_ORANGE):
#     if len < 10:
#         return
#     if width <= 2:
#         width = 2
#     if len < 12:
#         width = 9
#         color = sd.COLOR_GREEN
#     v1 = sd.get_vector(start_point=start_point, angle=angle + 30, length=len)
#     v1.draw(width=width, color=color)
#     v2 = sd.get_vector(start_point=start_point, angle=angle - 30, length=len)
#     v2.draw(width=width, color=color)
#     start_point = v1.end_point
#     draw_branches(start_point, angle + 30, len * .75, width - 2)
#     start_point = v2.end_point
#     draw_branches(start_point, angle - 30, len * .75, width - 2)
#
# draw_branches(start_point, 90, 100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

def draw_branches(starting_point, angle, length, width=10, color=sd.COLOR_ORANGE):
    if length < 10:
        return
    if width <= 2:
        width = 2
    if length < 15:
        width = 9
        color = sd.COLOR_GREEN
    v1 = sd.get_vector(start_point=starting_point, angle=angle + sd.random_number(17, 47), length=length)
    v1.draw(width=width, color=color)
    v2 = sd.get_vector(start_point=starting_point, angle=angle - sd.random_number(17, 47), length=length)
    v2.draw(width=width, color=color)
    start_point_v1 = v1.end_point
    start_point_v2 = v2.end_point
    random_len_v1 = sd.random_number(60, 90) / 100
    random_len_v2 = sd.random_number(60, 90) / 100
    draw_branches(start_point_v1, angle + 30, length * random_len_v1, width - 2)
    draw_branches(start_point_v2, angle - 30, length * random_len_v2, width - 2)


draw_branches(start_point, 90, 100)

# Пригодятся функции
# sd.random_number()

sd.pause()

# Зачёт!