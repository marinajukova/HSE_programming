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


def get_sentences(text):
    sentences = re.findall('<se>(.|\n)+?</se>', text)
    return sentences


def write_out_count_sentences(file_texts_dict):
    with open('amount of sentences.txt', 'w', encoding='utf-8') as f:
        for filename in file_texts_dict:
            text = file_texts_dict[filename]
            sent_am = len(get_sentences(text))
            f.writelines(filename+'\t'+str(sent_am)+'\n')
        

def get_words(raw_text):
##    <w><ana lex="центральный" gr="A=m,sg,loc,plen"></ana>центр`альном</w>
    word_list = []
    raw_lines = raw_text.split()
    word_lines = re.findall('(<w>.+?</w>)((?:\n?[«»,.! \?\-])*)', raw_text)
    for i in range(len(word_lines)):
        line = word_lines[i][0].strip('<w>').strip('</')
        ana, word = line.split('</ana>')
        ana = ana.strip('>').strip().strip('ana').strip()
        word_list.append([word] + [word_lines[i][1].strip().strip(' ')] + [ana])
    return word_list


def create_clear_text_out_of_words(word_list):
    text = []
    for el in range(len(word_list)):
        word = word_list[el]
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


def find_spec_bigr_in_sentence(word_list):
    spec_bigr = []
    for i in range(len(word_list)):
        word = word_list[i]
        if i > 0:
            previous_word = word_list[i-1]
            if 'loc' in word[2] and 'PR' in previous_word[2]:
                spec_bigr.append(previous_word[0]+' '+word[0])
    return spec_bigr


def find_all_spec_bigr(raw_texts_dict):
    sbec_bigr = []
    texts = raw_texts_dict.values
    for text in texts:
        sentences = get_sentences(text)
        for sentence in sentences:
            sentence_word_list = get_words(sentence)
            sentence_spec_bigr = find_spec_bigr_in_sentence(sentence_word_list)
            context = create_clear_text_out_of_words(sentence_word_list)
            for bigr in sentence_spec_bigr:
                sbec_bigr.append([bigr, context])
    return sbec_bigr


def write_out_spec_bigr(spec_bigr):
    with open('bigrams.txt', 'w', encoding='utf-8') as f:
        for bigr in spec_bigr:
            f.writelines(bigr[0]+'\t'+bigr[1]+'\n')
    


def main():
    raw_texts_dict = open_file_texts('news')
    write_out_count_sentences(raw_texts_dict) ##5
    file_meta = find_file_meta(raw_texts_dict)
    write_out_file_meta(file_meta) ##8
    


if __name__ == '__main__':
    main()
