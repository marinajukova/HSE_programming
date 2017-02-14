##  1. (5 баллов) Открыть файл с корпусом, подсчитать в нём число строк;
##  открыть другой файл для записи, записать туда число строк, найденных в файле с корпусом.
##  2. (8 баллов) Создать словарь, в котором ключами являются строки с морфологическим разбором слов
##  (то есть значения атрибута type для строк, в которых имеется "<w lemma="),
##  а значениями - количество их вхождений в файле. Распечатать ключи из словаря в открытый для записи файл (значения распечатывать не нужно).
##  3. (10 баллов) С помощью регулярных выражений найти и подсчитать все вхождения прилагательных во множественном числе
## (то есть таких разборов, в которых type=" начинается с "l" и содержит "f" на третьей позиции, например: type="lhfosf").
##  Результат подсчётов напечатать в другой открытый для записи файл таким образом, чтобы каждая пара "разбор - число вхождений" располагалась на одной строке.
##  Преобразуйте содержимое корпуса в формат csv. Запишите результат в новый файл следующим образом:
##  на одной строке должны находиться лемма, разбор, словоформа, разделенные запятыми.
##  Пунктацию и служебную информацию можно удалить.

import re


def openfile_lines(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
    return lines


def find_words(lines):
    words = []
    for i in range(len(lines)):
        if re.search('<w lemma=', lines[i]):
            words.append(lines[i])
    return words


def purify_info_about_words(words):
    pure = []
    lemmas = []
    types = []
    word_forms = []
    for i in range(len(words)):
        if re.search('lemma="(.+?)".*?type="(.+?)".*?>(.+?)<', words[i]):
            found_lemma = re.search('lemma="(.+?)".*?type="(.+?)".*?>(.+?)<', words[i]).group(1)
            found_type = re.search('lemma="(.+?)".*?type="(.+?)".*?>(.+?)<', words[i]).group(2)
            found_form = re.search('lemma="(.+?)".*?type="(.+?)".*?>(.+?)<', words[i]).group(3)
            pure.append([found_lemma, found_type, found_form])
    return pure

def count_forms(words):
    freq = {}
    for i in range(len(words)):
        form = re.search('type="(.+?)"', words[i]).group(1)
        if form not in freq:
            freq[form] = 1
        else:
            freq[form] += 1
    return freq


def plural_adjectives(freqs):
    forms = list(freqs.keys())
    pluradj = []
    for i in range(len(forms)):
        if re.search('l.f.*', forms[i]):
            adj_form = re.search('l.f.*', forms[i]).group()
            if adj_form:
                pluradj.append(adj_form)
    pluradj_freq = {}
    for i in range(len(pluradj)):
        pluradj_freq[pluradj[i]] = freqs[pluradj[i]]
    return pluradj_freq


def main():
    lines_dict = openfile_lines('dict.txt')
    word_list = find_words(lines_dict)
    pure_info = purify_info_about_words(word_list)
    freq_dict = count_forms(word_list)
    pluradj_freq_dict = plural_adjectives(freq_dict)
    with open('lines.txt', 'w', encoding = 'utf-8') as f: 
        f.write(str(len(lines_dict))) ##(5 баллов)
    with open('word forms.txt', 'w', encoding = 'utf-8') as f: 
        f.write('\n'.join(freq_dict.keys())) ##(8 баллов)
    with open('plural adjectives frequencies.txt', 'w', encoding = 'utf-8') as f:
        text = ''
        for key in pluradj_freq_dict:
            text += str(key)+' '+str(pluradj_freq_dict[key])+'\n'
        f.write(text)
    with open('dictionary.csv', 'w', encoding='utf-8') as f:
        header = ['лемма', 'грамматическая форма', 'словоформа']
        f.write(','.join(header)+'\n')
        for i in range(len(pure_info)):
            f.write(','.join(pure_info[i])+'\n') ##(10 баллов)
            

if __name__ == '__main__':
    main()
