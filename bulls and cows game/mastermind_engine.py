# -*- coding: utf-8 -*-

from random import sample

_hidden_number = ''


def make_number():
    global _hidden_number
    rand_list = '0123456789'
    _hidden_number = sample(rand_list, 5)
    if _hidden_number[0] != '0':
        del _hidden_number[-1]
        _hidden_number = ''.join(_hidden_number)
    else:
        del _hidden_number[0]
        _hidden_number = ''.join(_hidden_number)


def check_number(user_value):
    bulls_and_cows = {}
    count_bulls = 0
    count_cows = 0
    for i, element in enumerate(_hidden_number):
        if user_value[i] == element:
            count_bulls += 1
        elif user_value[i] in _hidden_number:
            count_cows += 1
    bulls_and_cows['bulls'] = count_bulls
    bulls_and_cows['cows'] = count_cows
    return bulls_and_cows
