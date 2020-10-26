## Интересные задачки и мини проекты из моего обучения

В этом репозитории находятся интересные ___на мой взгляд___ задачки и мини проекты с которыми мне приходилось <br/>
сталкиваться в процессе обучения.

[![](https://img.shields.io/static/v1?label=char_stat&message=.py&color=blueviolet)](book%20parser/char_stat.py)
считает статистику по буквам в любом текстовом файле (в моем случае роман "Война и Мир").<br/>
Входные параметры: файл для сканирования <br/>
Статистику считает только для букв алфавита. Выводит на консоль упорядоченную статистику.


[![](https://img.shields.io/static/v1?label=mastermind&message=.py&color=blueviolet)](bulls%20and%20cows%20game/mastermind.py)
Игра [«Быки и коровы»](https://goo.gl/Go2mb9) <br/>
__Задача:__<br/>
Составить отдельный модуль [_mastermind_engine_](bulls%20and%20cows%20game/mastermind_engine.py), реализующий функциональность игры.<br/>
В mastermind_engine нужно реализовать функции:<br/>
   - загадать_число()
   - проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
   
В текущем модуле _mastermind_ реализовать логику работы с пользователем.

[![](https://img.shields.io/static/v1?label=sort_file&message=.py&color=blueviolet)](sort%20the%20files/sort_file.py)
скрипт для упорядочивания файлов <br/>
__Задача:__<br/>
 Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)<br/>
 Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
 Например, так:
   - исходная папка<br/>
       >icons/cat.jpg<br/>
       icons/man.jpg<br/>
       icons/new_year_01.jpg
   - результирующая папка
       >icons_by_year/2018/05/cat.jpg<br/>
       icons_by_year/2018/05/man.jpg<br/>
       icons_by_year/2017/12/new_year_01.jpg

 Входные параметры основной функции: папка для сканирования, целевая папка.