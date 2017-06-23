## 5 баллов:
##    Посчитайте, сколько в каждом файле предложений, запишите эту информацию в новый текстовый файл в формате
##    "название файла<табуляция>количество предложений", для каждого файла информация на новой строчке.
##
## 8 баллов:
##    Создайте csv-таблицу с полями "Название файла", "Автор", "Тематика текста" (topic),
##    содержащую информацию о всех статьях (эту информацию можно найти в метаданных). Пример таблицы ниже.
##
## Название файла	Автор	                Тематика текста
## file.xhtml	        Батюшков Константин	искусство и культура
##
## 10 баллов:
##    Найдите в текстах все биграммы вида "предлог + существительное в предл. пад.".
##    В новый текстовый файл запишите найденные биграммы; на каждой строке нужно записать биграмму и предложение, в котором она встретилась,
##    разделив их табуляцией. Повторяющиеся биграммы убирать не надо.

import os
import re
import csv


def open_file_texts(directory):
    raw_texts_dict = {}
    for root, dirs, files in os.walk(directory):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='windows-1251') as t:
                text = t.read()
                raw_texts_dict[f] = text
    return raw_texts_dict


def count_sentences(text):
    sentences = re.findall('<se>(.|\n)+?</se>', text)
    return len(sentences)


def write_out_count_sentences(file_texts_dict):
    with open('amount of sentences.txt', 'w', encoding='utf-8') as f:
        for filename in file_texts_dict:
            text = file_texts_dict[filename]
            sent_am = count_sentences(text)
            f.writelines(filename+'\t'+str(sent_am)+'\n')
        

def get_words(raw_text):
    word_arr = []
    raw_lines = raw_text.split()
    word_lines = re.findall('(<w>.+?</w>)((?:\n?[«»,.! \?\-])*(?:\n?[01234567])*)', raw_text)
    for i in range(len(word_lines)):
        line = word_lines[i][0].strip('<w>').strip('</').split('<ana')
        for e in range(len(line)):
            if e > 0:
                line[e] = line[e].strip(' />')
        word_arr.append([line[0]] + [len(line)-1] + [word_lines[i][1].strip().strip(' ')] + line[1:])
    return word_arr


def create_clear_text_out_of_words(word_arr):
    text = []
    for el in range(len(word_arr)):
        word = word_arr[el]
        d = re.match('\d+', word[2])
        if '«' in word[2]:
            text.append(word[0] + ' «')
        elif d:
            text.append(word[0] + ' ' + d.group(0) +' ')
        else:
            text.append(word[0] + word[2] + ' ')
    return text


def find_file_meta (file_texts_dict):
    file_meta_list = []
    for filename in file_texts_dict:
        text = file_texts_dict[filename]
        author = re.search('<meta content="(.+)" name="author"></meta>', text)
        if author:
            author = re.search('<meta content="(.+)" name="author"></meta>', text).group(1)
        topic = re.search('<meta content="(.+)" name="topic"></meta>', text)
        if topic:
            topic = re.search('<meta content="(.+)" name="topic"></meta>', text).group(1)
        file_meta_list.append([filename, author, topic])
    return file_meta_list

def write_out_file_meta (file_meta_list):
    with open('file metadata.csv', 'w', encoding='utf-8') as n:
        text = csv.writer(n, delimiter=';')
        header = ['Название файла', 'Автор', 'Тематика текста']
        text.writerow(header)
        for row in file_meta_list:
            text.writerow(row)

def main():
    raw_texts_dict = open_file_texts('news')
    write_out_count_sentences(raw_texts_dict) ##5
    file_meta = find_file_meta(raw_texts_dict)
    write_out_file_meta(file_meta) ##8
    


if __name__ == '__main__':
    main()
