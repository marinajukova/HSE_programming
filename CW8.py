##1) Написать фкнкцию opentext():
##    - открывать файл с названием fname
##            with open()
##    - перевести текст в нижний регистр
##            text.lower()
##    - делить текст на слова (между пробелами и знаками препинания)
##            text.split()
##    - удалить от слов знаки препинания
##            text.strip('.,?*()')
##    - возвращать массив всех словоформ в тексте
##            return

def opentext(fname):
    forms = []
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    forms = text.split()
    for i in range(len(forms)):
        forms[i] = forms[i].strip('.,?*()«»')
    return forms

##2) функция first_letter(letter, fname)
##    - возвращает массив слов из текста, которые начинаются на букву letter
##    - обязательно использовать функцию opentext()

def first_letter(letter, fname = 'text.txt'):
    starting_with_letter = []
    forms = opentext(fname)
    for i in range(len(forms)):
        if forms[i][0] == letter:
            starting_with_letter.append(forms[i])
    return starting_with_letter

##3) функция questions()
##    - спрашивает буву и имя файла и число
##    - печатает результат first_letter(letter) для этого файла, но только те слова, длина которых больше введённого числа

def questions():
    fname = input('Введите имя файла: ')
    letter = input('Введите букву: ')
    number = int(input('Введите целое число: '))
    starting_with_letter = first_letter(letter, fname)
    answer = []
    for i in range(len(starting_with_letter)):
        if len(starting_with_letter[i]) > number:
            answer.append(starting_with_letter[i])
    return answer

##4) функция adjectives(fname)
##    - находит в русском тексте прилагательные в именительном падеже с окончаниями "ый" "ий" "ой" "ая" "яя" "ое" "ее"
##    - распечатать пары прилагательное с следующим за ним словом

def adjectives(fname):
    forms = opentext(fname)
    adj = []
    for i in range(len(forms)):
        if len(forms[i]) > 2:
            if forms[i][-1] == 'й':
                if forms[i][-2] == 'o' or forms[i][-2] == 'ы' or forms[i][-2] == 'и':
                    if i != len(forms)-1:
                        adj.append(forms[i]+' '+forms[i+1])
                    else:
                        adj.append(forms[i])
            elif forms[i][-1] == 'я':
                if forms[i][-2] == 'а' or forms[i][-2] == 'я':
                    if i != len(forms)-1:
                        adj.append(forms[i]+' '+forms[i+1])
                    else:
                        adj.append(forms[i])
            elif forms[i][-1] == 'е':
                if forms[i][-2] == 'o' or forms[i][-2] == 'е':
                    if i != len(forms)-1:
                        adj.append(forms[i]+' '+forms[i+1])
                    else:
                        adj.append(forms[i])
    return adj

print(adjectives('text.txt'))
