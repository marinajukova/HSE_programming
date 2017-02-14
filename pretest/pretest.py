## 5 баллов:
##    открыть файл, посчитать в нем количество слов. Распечатать это количество.
## 8 баллов:
##    создать частотный словарь для всех слофоворм, встретившихся в тексте.
##    Распечатать его в отдельный csv-файл, отсортировав по алфавиту (на каждой строчке слово + запятая + количество вхождений).
## 10 баллов:
##    найти все вхождения конструкции род. падеж прилагательного c безударн. окончанием -аго + род. падеж сущ. 1 или 2 скл.
##    (например, великорусскаго языка) в файле. Выписать в отдельный файл найденные конструкции и их контексты -
##    3 слова слева и 3 слова справа (каждая конструкция и её контекст на отдельной строчке).

import re
import csv

def openforms(text):
    forms = []
    text = text.lower()
    forms = text.split()
    for i in range(len(forms)):
        forms[i] = forms[i].strip('.,?*()«»!\'\":; ')
    return forms


def freqlist(forms):
    freqs = {}
    for i in range(len(forms)):
        if forms[i] not in freqs:
            freqs[forms[i]] = 1
        else:
            freqs[forms[i]] +=1
    return freqs


def freqlist_to_csv(freqs):
    with open('freq.csv', 'w', encoding='utf-8') as f:
        output = csv.writer(f, delimiter=',')
        header = ['слово', 'частота']
        output.writerow(header)
        for key in sorted(freqs):
            output.writerow([key, freqs[key]])


def agosforms(text):
    agos = re.findall('(?:(?:[А-Яа-яіѢѣЁё])+[\s,.!\?:;"\(\)\'»\n\t—]+?){3}[А-Яа-яiѢѣ]+?аго [А-Яа-яiѢѣ]+?(?:а|и)[\s,.!\?:;"\(\)\'»\n\t—]{,5}(?:[А-Яа-яiѢѣ]+?[\s,.!\?;:—"\(\)\'»\n\t]+?){3}',text)
    with open('agos.txt', 'w', encoding='utf-8') as f:
        output = f.write('\n'.join(agos))


def main():
    with open ('Лесков.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
    forms = openforms(text)
    print(len(forms)) ## 5
    freqs = freqlist(forms)
    freqlist_to_csv(freqs) ##8
    agosforms(text) ##10

if __name__ == '__main__':
    main()
