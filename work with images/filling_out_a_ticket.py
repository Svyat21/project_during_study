# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse


def get_arguments():
    human_args = argparse.ArgumentParser(description='filling out the ticket')
    human_args.add_argument('fio', type=str, help='enter your fio')
    human_args.add_argument('from_', type=str, help='where are you flying from')
    human_args.add_argument('to', type=str, help='where are you going')
    human_args.add_argument('date', type=str, help='date of departure')
    human_args.add_argument('--save_ticket', type=str, default='images/probe.png', help='where to save it?')
    return human_args.parse_args()


class MakeTicket:

    def __init__(self, data):
        self.fio = data.fio
        self.from_ = data.from_
        self.to = data.to
        self.date = data.date
        self.save = data.save_ticket

    def run(self):
        im = Image.open('images/ticket_template.png')

        draw = ImageDraw.Draw(im)

        font_path = 'ofont_ru_Intro Script Demo.ttf'
        font = ImageFont.truetype(font_path, size=20)

        y = ((im.size[1] // 3) - font.size // 2) + 2
        draw.text((44, y), self.fio, font=font, fill=ImageColor.colormap['black'])
        y += 72
        draw.text((44, y), self.from_, font=font, fill=ImageColor.colormap['black'])
        y += 65
        draw.text((44, y), self.to, font=font, fill=ImageColor.colormap['black'])
        draw.text((287, y), self.date, font=font, fill=ImageColor.colormap['black'])

        im.save(self.save)
        print('Билет заполнен!')


if __name__ == '__main__':
    human_data = get_arguments()
    ticket = MakeTicket(human_data)
    ticket.run()

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
