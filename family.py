# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


# ####################################################### Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

class Man:
    food_eaten = 0
    stroking_the_cat = 0

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return '{}, степень сытости - {}, степень счастья - {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        self.fullness += 30
        self.house.food_in_the_fridge -= 30
        self.food_eaten += 30
        print(f"{self.name} - покушал(а).")

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10
        self.stroking_the_cat += 1
        print(f'{self.name}, весь день гладил(а) кота.')

    def checking_a_persons_condition(self):
        if self.happiness < 10:
            cprint('{}, умер(ла) от депрессии!'.format(self.name), color='red')
            return False
        elif self.fullness <= 0:
            cprint('{}, умер(ла) от голода!'.format(self.name), color='red')
            return False
        elif self.house.mess >= 90:
            self.happiness -= 10
        self.house.mess += 5


class House:

    def __init__(self):
        self.money_in_the_safe = 100
        self.food_in_the_fridge = 50
        self.food_for_the_cat = 30
        self.mess = 0

    def __str__(self):
        return 'Денег в сейфе - {}, еды в холодильнике - {}, еды для кота - {}, количество грязи - {}'.format(
            self.money_in_the_safe, self.food_in_the_fridge, self.food_for_the_cat, self.mess)


class Husband(Man):
    gaming_days = 0
    money_earned = 0

    def __str__(self):
        return 'Муж: ' + super().__str__()

    def work(self):
        self.house.money_in_the_safe += 150
        self.fullness -= 10
        self.money_earned += 150
        print(f'{self.name}, сходил на работу и положил деньги в тумбочку.')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        self.gaming_days += 1
        print(f'{self.name}, целый день играл в "танки".')

    def act(self):
        toss_a_coin = randint(0, 2)
        if super().checking_a_persons_condition() is not None:
            return 'Конец.'
        elif self.fullness <= 10:
            super().eat()
        elif self.house.money_in_the_safe <= 360:
            self.work()
        elif self.happiness <= 50:
            self.gaming()
        elif toss_a_coin == 2:
            self.work()
        elif toss_a_coin == 1:
            super().pet_the_cat()
        else:
            self.gaming()

    def personal_statistics(self):
        cprint(f'{self.name} играл в танки - {self.gaming_days} дней, '
               f'заработал - {self.money_earned} едениц денег, гладил кода {self.stroking_the_cat} дней, '
               f'съел - {self.food_eaten} едениц еды', color='yellow')


class Wife(Man):
    bought_fur_coats = 0
    cleaning_operations = 0
    purchased_food = 0
    purchased_food_for_the_cat = 0

    def __str__(self):
        return 'Жена: ' + super().__str__()

    def shopping(self):
        self.house.food_in_the_fridge += 90
        self.fullness -= 10
        self.purchased_food += 90
        print(f'{self.name}, сходила в магазин за продуктами.')

    def to_buy_food_for_the_cat(self):
        self.house.food_for_the_cat += 30
        self.fullness -= 10
        self.house.money_in_the_safe -= 30
        self.purchased_food_for_the_cat += 30
        print(f'{self.name} купила еду для кота.')

    def buy_fur_coat(self):
        if self.house.money_in_the_safe >= 350:
            self.happiness += 60
            self.fullness -= 10
            self.house.money_in_the_safe -= 350
            self.bought_fur_coats += 1
            print(f'{self.name}, купила себе новую шубу.')
        else:
            self.fullness -= 10
            print(f'{self.name}, весь день ходила по магазинам, хотела купить себе новую шубу, но не хватило денег.')

    def clean_house(self):
        if self.house.mess > 100:
            self.house.mess -= 100
        else:
            self.house.mess -= self.house.mess
        self.fullness -= 10
        self.cleaning_operations += 1
        print(f'{self.name}, сделала уборку в доме.')

    def act(self):
        toss_a_coin = randint(0, 3)
        if super().checking_a_persons_condition() is not None:
            return cprint('Конец.', color='yellow')
        elif self.fullness <= 10:
            super().eat()
        elif self.house.food_in_the_fridge <= 60:
            self.shopping()
        elif self.house.food_for_the_cat <= 20:
            self.to_buy_food_for_the_cat()
        elif self.house.mess >= 80:
            self.clean_house()
        elif self.happiness <= 50:
            self.buy_fur_coat()
        elif toss_a_coin == 3:
            self.shopping()
        elif toss_a_coin == 2:
            self.clean_house()
        elif toss_a_coin == 1:
            super().pet_the_cat()
        else:
            self.buy_fur_coat()

    def personal_statistics(self):
        cprint(f'{self.name}, купила себе - {self.bought_fur_coats} шуб,'
               f' сделала уборку - {self.cleaning_operations} раз,'
               f' купила в магазине - {self.purchased_food} едениц еды,'
               f' купила - {self.purchased_food_for_the_cat} ед. еды для кота,'
               f' гладила кота {self.stroking_the_cat} дней, съела - {self.food_eaten} едениц еды', color='yellow')


# ####################################################### Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:
    ate_food = 0
    slept_for_days = 0
    ruined_the_wallpaper = 0

    def __init__(self, name, house=None):
        self.name = name
        self.fullness = 30
        self.house = house

    def __str__(self):
        return 'Кот {}, степень сытости - {}'.format(self.name, self.fullness)

    def act(self):
        toss_a_coin = randint(0, 1)
        if self.fullness <= 0:
            cprint('Кот {}, умер от голода!'.format(self.name), color='red')
            return 'Кота {}, больше с нами нет.'.format(self.name)
        elif self.fullness <= 10:
            self.eat()
        elif toss_a_coin == 1:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        self.fullness += 20
        self.house.food_for_the_cat -= 10
        self.ate_food += 10
        print('Кот {}, поел.'.format(self.name))

    def sleep(self):
        self.fullness -= 10
        self.slept_for_days += 1
        print('Кот {}, весь день спал.'.format(self.name))

    def soil(self):
        self.fullness -= 10
        self.house.mess += 5
        self.ruined_the_wallpaper += 1
        print('Кот {}, весь день дрял обои.'.format(self.name))

    def personal_statistics(self):
        cprint('Кот - {} спал - {} дней, съел - {} едениц еды, драл обои - {} дней'.format(
            self.name, self.slept_for_days, self.ate_food, self.ruined_the_wallpaper), color='yellow')


# ######################################################## Часть вторая бис
# #
# # После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
# #
# # Ребенок может:
# #   есть,
# #   спать,
# #
# # отличия от взрослых - кушает максимум 10 единиц еды,
# # степень счастья  - не меняется, всегда ==100 ;)


class Child(Man):
    slept_for_days = 0

    def __str__(self):
        return 'ребенок: ' + super().__str__()

    def act(self):
        toss_a_coin = randint(0, 1)
        if self.fullness <= 0:
            return cprint('Ребенок {} - умер :(', color='yellow')
        elif self.fullness <= 10:
            self.eat()
        elif toss_a_coin == 1:
            self.sleep()
        else:
            self.eat()

    def eat(self):
        self.fullness += 10
        self.house.food_in_the_fridge -= 10
        self.food_eaten += 10
        print(f'{self.name} покушал.')

    def sleep(self):
        self.fullness -= 10
        self.slept_for_days += 1
        print(f'{self.name} Весь день спал.')

    def personal_statistics(self):
        cprint('Ребенок {} спал - {} дней, съел - {} едениц еды'.format(
            self.name, self.slept_for_days, self.food_eaten), color='yellow')


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
barsik = Cat(name='Барсик', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    barsik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(barsik, color='cyan')
    cprint(home, color='cyan')
serge.personal_statistics()
masha.personal_statistics()
kolya.personal_statistics()
barsik.personal_statistics()


# ######################################################## Часть третья
# #
# # после подтверждения учителем второй части (обоих веток)
# # влить в мастер все коммиты из ветки develop и разрешить все конфликты
# # отправить на проверку учителем.
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

# Зачёт!
