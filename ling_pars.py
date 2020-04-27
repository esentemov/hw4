# Использовался код парсера сайта 7english.ru для получения списка англо-русского словаря
# Добавлена мини-игра, где компьютер, из полученного списка, выбирает слово на англ. и просит ввести перевод на русском

# -*- coding: utf8 -*-
import requests
import random

rs = requests.get('http://www.7english.ru/dictionary.php?id=2000&letter=all')

from bs4 import BeautifulSoup

root = BeautifulSoup(rs.content, 'html.parser')

en_ru_items = []

for tr in root.select('tr'):
    if 'onmouseover' not in tr.attrs:
        continue

    td_list = [td.text.strip() for td in tr.select('td')]

    # Количество ячеек в таблице со словами -- 9
    if len(td_list) != 9 or not td_list[1] or not td_list[5]:
        continue

    en = td_list[1]

    ru = td_list[5].split(', ')[0]

    en_ru_items.append((en, ru))

print(en_ru_items)
dictionary = dict(en_ru_items)
# Переводим в словарь

errors = 0
bonus = 0

print("Пора потренироваться, ошибок у нас не более 3")

for keys in random.sample(dictionary.keys(), len(dictionary)):
    print('Введите значение слова: ' + str(keys))
    answer = input("Вы считаете, что это слово переводится как ").lower().strip()
    if dictionary[keys] == answer:
        bonus += 1
        print("Отлично, ваш счет составляет :", bonus)
    elif errors > 2:
        print("game over")
        break
    else:
        errors += 1
        print("Количество ошибок", errors)