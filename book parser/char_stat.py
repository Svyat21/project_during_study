# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import collections
import os
import zipfile
from operator import itemgetter


class StatisticsByLetter:

    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path

    def unpacking_zip_archives(self):
        zip_fail_path = os.path.normpath(self.file_path)

        zfile = zipfile.ZipFile(os.path.join(zip_fail_path, self.file_name), 'r')
        for element in zfile.namelist():
            zfile.extract(element)
            self.file_name = element

    def file_analysis(self):
        pass

    def total_sort(self):
        pass

    def print_statistics(self):
        pass

    def analysis(self):
        if self.file_name.endswith('.zip'):
            self.unpacking_zip_archives()
        self.file_analysis()
        self.total_sort()
        self.print_statistics()


class CountingLetters(StatisticsByLetter):

    def __init__(self, file_name, file_path, sort_alpha=False, sort_reverse=False):
        super().__init__(file_name=file_name, file_path=file_path)
        self.stat = collections.defaultdict(int)
        self.totals = []
        self.count = 0
        self.sort_alpha = sort_alpha
        self.sort_reverse = sort_reverse

    def file_analysis(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if not char.isalpha():
                        continue
                    self.stat[char] += 1

        for char, count in self.stat.items():
            if 1040 <= ord(char) <= 1103:
                self.totals.append((count, char))

    def total_sort(self):
        if self.sort_alpha:
            self.totals.sort(key=itemgetter(1), reverse=self.sort_reverse)
        else:
            self.totals.sort(reverse=self.sort_reverse)

    def print_statistics(self):
        print(f'+{"-" * 9}+{"-" * 9}+')
        print(f'|{"буква":^9}|{"частота":^9}|')
        print(f'+{"-" * 9}+{"-" * 9}+')
        for element in self.totals:
            self.count += element[0]
            print(f'|{element[1]:^9}|{element[0]:^9}|')
        print(f'+{"-" * 9}+{"-" * 9}+')
        print(f'|{"итого:":^9}|{self.count:^9}|')
        print(f'+{"-" * 9}+{"-" * 9}+')


filename = 'voyna-i-mir.txt.zip'
filepath = 'python_snippets'
catterer = CountingLetters(file_name=filename, file_path=filepath, sort_alpha=True, sort_reverse=True)
catterer.analysis()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию

# Зачёт!