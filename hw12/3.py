## 3. Нужно взять какой-нибудь файл с достаточно большим текстом, прочитать его,
## поделить на предложения (просто по знакам конца предложения), удалить знаки препинания.
## Затем сделать следующее (обязательно использовать list comprehensions и formatting):
## Преобразовать все предложения в тексте, после каждого слова дописав его длину в символах через подчеркивание. Так, "Мама вымыла раму" превращается в 
## Мама_4 
## вымыла_6 
## раму_4


import re


def open_text_phrases(fname):
    phrases = []
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = re.sub('\.\.\.|[\.\?]', '!', text)
    phrases = text.split('!')[:-1]
    for i in range(len(phrases)):
         phrases[i] = re.sub('[<>\*\.«»,\'\"]','', phrases[i])
         phrases[i] = phrases[i].strip()
    return phrases


def main():
    phrase_list = open_text_phrases('text.txt')
    word_length_list = [[w, len(w)] for phrase in phrase_list for w in phrase.split()]
    template = '{}_{}'
    for word in word_length_list:
        print(template.format(word[0], word[1]))
        

if __name__ == '__main__':
    main()
