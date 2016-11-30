##Про работу с файлами
##Однобайтовые кодировки 256 1 байт (8 знаков) - 1 знак
##Двухбайтовый кодировки 65 тыс
##Четырёхбайтовые кодировки 4 млн
##Юникод таблица с кучей символов: двухбайтовые - utf-8, четырёхбайтовые utf-16
##Для кириллицы основные - utf-8, CP(windows)1251 = ANSI, KOI-8

##'mother\'s' - бекслеш защищает символ
##Программа загадывает слова из списка в рандомном порядке
##import random
##words = ['холодно','страшно','больно','противно','безвыходно','горько','пугающе']
##for word if words:
##    word = random.choice(words)
##    response = input('Какое слово я загадала?')
##    if response == word:
##        print('Правильно!')
##    else:
##        print('Нет, слово было', word)

##Открыть, прочитать, закрыть и напечатать текстовый файл их той же папки
##f = open('words.txt','r', encoding = 'utf-8')
##text = f.read()
##f.close()
##print(text)

##with open('words.txt','r', encoding = 'utf-8') as f: ## Открыть и закрыть файл автоматически и прочитать как переменную f
##    text = f.readlines() ##Всё равно что    text = f.read() и lines = text.split('\n')
##print(text)

##with open('words.txt','r', encoding = 'utf-8') as f:
##    for line in f: ## читать по строкам
##        line = line.strip() ## strip() откусывает по умолчанию перенос строки с конца или с начала строки, но можно задать в скобках, какие символы надо откусывать

import random

with open('words.txt','r', encoding = 'utf-8') as f:
    lines = f.readlines()
    lenlines = len(lines)
    random.shuffle(lines)
    score = 0
    for line in lines:
        line = line.strip() 
        word, hint = line.split(' ',1) ## строка разделенная по пробелу 1 раз
        response = input('Какое слово я загадала?\n'+
                         'Подсказка: '+hint+' ')
        if response == word:
            print('Правильно!')
            score += 1
        else:
            print('Нет, слово было', word)

with open('scores.txt', 'w', encoding = 'utf-8') as n: ## Создаёт или заменяет существующий файл той же папке с этим именем. Если дать в качестве второго аргумента 'a', то он будет пытаться дописывать в конец существующего файла с этим именем
    percent = score/lenlines*100
    n.write('Вот результат: ')
    n.write(str(percent)+'%')
