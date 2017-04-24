## Напишите программу, которая
##  получает на вход путь к какой-либо папке,
##  находит в этой папке и ее подпапках все файлы с расширением .txt,
##  собирает словарь, в котором для всех словоформ из всех текстов записано количество вхождений,
##  распечатывает 10 самых частых словоформ.
## Делите код на функции, используйте дебаггер для поиска ошибок.

import os, codecs


def open_file(title):
    a = codecs.open(title, 'r', 'utf-8')
    words = [word.strip(' ,.?!-:;').lower() for word in a.read().split()]
    return words


def count_word_frequency(words):
    freq_dict = {}
    for word in words:
        try:
            freq_dict[word] += 1
        except KeyError:
            freq_dict[word] = 1
    return freq_dict


def find_max_keys(dict_num_values, amount):
    values_list = dict_num_values.values()
    max_values = []
    i = 0
    while i < amount:
        local_max = max(values_list)
        max_values.append(local_max)
        if local_max != 1:
            values_list = [x for x in values_list if x != local_max]
        i += 1
    max_keys = []
    for key in dict_num_values:
        if dict_num_values[key] in max_values:
            max_keys.append(key)
    return max_keys


def extract_words_from_txt_in_folder(path):
    words = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if len(f.split('.')) == 2:
                file_name = f.split('.')[0]
                file_ext = f.split('.')[1]
                if file_ext == 'txt':
                    words += open_file(os.path.join(root, f))
    return words

def main():
    print(find_max_keys(count_word_frequency(extract_words_from_txt_in_folder('.')),10))


if __name__ == "__main__":
    main()
