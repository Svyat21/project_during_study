## Интересные задачки и мини проекты из моего обучения

В этом репозитории находятся интересные ___на мой взгляд___ задачки и мини проекты с которыми мне приходилось <br/>
сталкиваться в процессе обучения.

[![mastermind.py](https://img.shields.io/static/v1?label=char_stat&message=.py&color=blueviolet)](book%20parser/char_stat.py)
считает статистику по буквам в любом текстовом файле (в моем случае роман "Война и Мир").<br/>
Входные параметры: файл для сканирования <br/>
Статистику считает только для букв алфавита. Выводит на консоль упорядоченную статистику.


[![mastermind.py](https://img.shields.io/static/v1?label=mastermind&message=.py&color=blueviolet)](bulls%20and%20cows%20game/mastermind.py)
Игра [«Быки и коровы»](https://goo.gl/Go2mb9) <br/>
__Задача:__<br/>
Составить отдельный модуль [_mastermind_engine_](bulls%20and%20cows%20game/mastermind_engine.py), реализующий функциональность игры.<br/>
В mastermind_engine нужно реализовать функции:<br/>
   - загадать_число()
   - проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
   
В текущем модуле _mastermind_ реализовать логику работы с пользователем.