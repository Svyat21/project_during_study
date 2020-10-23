# -*- coding: utf-8 -*-

import os
import shutil
import time


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class FileSorter:

    def __init__(self, folder_to_scan, target_folder=None):
        self.folder_to_scan = folder_to_scan
        self.target_folder = target_folder
        self.file_list = []

    def scanning_a_folder(self):
        pass

    def moving_to_a_target(self):
        pass

    def proceed(self):
        self.scanning_a_folder()
        self.moving_to_a_target()


class SortingPhotos(FileSorter):

    def scanning_a_folder(self):
        generator_object = os.walk(self.folder_to_scan)
        for path, dirs, files in generator_object:
            for element in files:
                path_file = os.path.join(path, element)
                self.file_list.append(path_file)
        print(len(self.file_list))

    def moving_to_a_target(self):
        for file in self.file_list:
            mod_file = os.path.getmtime(file)
            gm_mod_file = time.gmtime(mod_file)
            path = os.path.normpath(os.path.join(self.target_folder, str(gm_mod_file.tm_year), str(gm_mod_file.tm_mon)))
            if os.path.exists(path) is not True:
                os.makedirs(path)
            shutil.copy2(file, path)


sort_photo = SortingPhotos('icons', 'icons_by_year')
sort_photo.proceed()


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html

# Зачёт!
