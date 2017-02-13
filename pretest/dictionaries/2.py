## Нужно взять файл, сделать из него русско-латинский и латинско-русский словарь следующего вида:
## Ключами должны быть индивидуальные слова, а значениями их переводы.
## Если у нескольких слов одинаковый перевод, нужно разделить их и сделать отдельными ключами: {'ille': 'тот', 'illa': 'тот', 'illud': 'тот'}.
## Если у слова есть несколько переводов, то нужно склеить их все в одно значение: {'тот': 'ille, illa, illud'}
## В русско-латинском словаре ключи - руские слова, значения - их латинские переводы, в латинско-русском наоборот.

import re

def revert(dictionary):
    reverted = {}
    for key in dictionary:
        reverted[dictionary[key]] = key
    return reverted


def russian_to_latin_dictionary(lines):
    raw = {}
    rus_to_lat = {}
    for i in range(len(lines)):
        raw[lines[i].split(' — ')[0]] = lines[i].split(' — ')[1].strip('\n')
    raw = revert(raw)
    for key in raw:
        if len(key.split(',')) > 1:
            for i in range(len(key.split(','))):
                rus_to_lat[key.split(',')[i-1].strip()] = raw[key]
                i +=10
        else:
            rus_to_lat[key] = raw[key]
    return rus_to_lat


def latin_to_russian_dictionary(lines):
    raw = {}
    lat_to_rus = {}
    for i in range(len(lines)):
        raw[lines[i].split(' — ')[0]] = lines[i].split(' — ')[1].strip('\n')
    for key in raw:
        if len(key.split(',')) > 1:
            for i in range(len(key.split(','))):
                lat_to_rus[key.split(',')[i-1].strip()] = raw[key]
                i +=10
        else:
            lat_to_rus[key] = raw[key]
    return lat_to_rus


def main():
    with open ('latin.txt', 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = re.sub('(?:–|−|-)', '—', lines[i])
            lines[i] = re.sub(';', ',', lines[i])
    print(latin_to_russian_dictionary(lines))
    print(russian_to_latin_dictionary(lines))

    
if __name__ == '__main__':
    main()
