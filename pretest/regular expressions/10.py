## В файле содержится пример речи человека, страдающего афазией -- нарушением речи.
## Удалите с помощью регулярных выражений все повторяющиеся слова, учитывая, что они могут быть разделены знаками препинания.

import re

def main():
    with open('aphasy.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower() ## Честно признаюсь, как сделать это с re.I до конца не разобралась.
    clear = re.sub('(\w+)(?:,?|\.*?) \\1', '\\1', text)
    while re.sub('(\w+)(?:,?|\.*?) \\1', '\\1', clear) != clear:
        clear = re.sub('(\w+)(?:,?|\.*?) \\1', '\\1', clear)
    print(clear)

if __name__ == '__main__':
    main()
