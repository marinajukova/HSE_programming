## 5 баллов:
## Посчитайте среднее количество разборов (тэг ana) на слово (тэг w).
##
## 8 баллов:
## Составьте частотный словарь всех частей речи в тексте. Например: {'APRO': 5, 'S': 277, ...}.
## Распечайте содержимое словаря в отдельный файл (на каждой строке "часть речи"<табуляция>"частотность").
##
## 10 баллов:
## Найдите в тексте все существительные в творительном падеже (обратите внимание, что некоторые разборы омонимичные.
## Если хотя бы один разбор с указанием творительного падежа присутствует, слово берём).
## Запишите в отдельный файл найденные существительные и контекст их употребления в таком формате:
##      3 слова слева<табуляция>найденное существительное<табуляция>3 слова справа.
## За сохранение знаков препинания отдельный плюс.

import re
import csv

def open_file(name):
    with open(name, 'r', encoding='utf-8') as f:
        file_text = f.read()
    return file_text


def get_words(raw_text):
    word_arr = []
    raw_lines = raw_text.split()
    word_lines = re.findall('(<w>.+</w>)((?:\n?[«»,.! \?\-])*(?:\n?[01234567])*)',raw_text)
    for i in range(len(word_lines)):
        line = word_lines[i][0].strip('<w>').strip('</').split('<ana')
        for e in range(len(line)):
            if e > 0:
                line[e] = line[e].strip(' />')
        word_arr.append([line[0]] + [len(line)-1] + [word_lines[i][1].strip().strip(' ')] + line[1:])
    return word_arr


def count_average_anas(word_arr):
    total = 0
    average = 0
    for i in range(len(word_arr)):
        total += word_arr[i][1]
    average = total/len(word_arr)
    return average



def count_all_pos(word_arr):
    pos_dict = {}
    for i in range(len(word_arr)):
        for el in range(len(word_arr[i])):
            if el > 2:
                pos = re.search('gr="(\w+)' , word_arr[i][el]).group(1)
                if pos not in pos_dict:
                    pos_dict[pos] = 1
                else:
                    pos_dict[pos] += 1
    with open('parts of speech frequency.txt', 'w', encoding='utf-8') as f:
        for pos in pos_dict:
            f.writelines(pos+'\t'+str(pos_dict[pos])+'\n')
    return pos_dict


def find_all_instr(word_arr):
    instr_words_dict = {}
    text = []
    for el in range(len(word_arr)):
        word = word_arr[el]
        if re.match('«|\d', word[2]):
            text.append(word[0]+' '+word[2])
        else:
            text.append(word[0]+word[2])
    for n in range(len(word_arr)):
        word = word_arr[n]
        for i in range(len(word)):
            if i > 1:
                instr = re.search('ins', word[i])
                if instr:
                    if word[0] not in instr_words_dict:
                        instr_words_dict[word[0]] = n 
    with open('words in instrumentalis.txt', 'w', encoding='utf-8') as f:
        for word in instr_words_dict:
            x = instr_words_dict[word] 
            if x-3 >= 0 and x+3 < len(text):
                f.writelines(' '.join(text[x-3:x])+'\t'+word+'\t'+' '.join(text[x+1:x+4])+'\n')
    return instr_words_dict


def main():
    raw_text = open_file('text.xml')
    word_arr = get_words(raw_text)
    average_anas = count_average_anas(word_arr)
    print(average_anas) ## 5
    count_all_pos(word_arr) ## 8
    find_all_instr(word_arr) ##10


if __name__ == '__main__':
    main()
