## В следующих 6 заданиях надо открыть файл с текстом на русском языке, а затем...

import re

def three_consonants(text): ## 1. Найти в тексте слова, в которых есть три согласных подряд.
    cons3 = re.findall('[^\s,.!\?:"\(\)\'«»\n]*?[йцкнгшщзхфвпрлджчсмтб]{3}.+?[\s,.!\?:"\(\)\'»\n]', text, re.I)
    for i in range(len(cons3)):
        cons3[i] = cons3[i].strip('\s,.!\?:"\(\)\'»\n\t ')
    return cons3
def startwith(text): ## 2. Найти все слова, которые начинаются с а или о, а вторая буква -- б или в.
    abcs = re.findall('[\s,.!\?:"\(\)\'«\n ](?:а|о)(?:б|в).+?[\s,.!\?:"\(\)\'»\n]', text, re.I)
    for i in range(len(abcs)):
        abcs[i] = abcs[i].strip('\s,.!\?:"\(\)\'»\n\t')
    return abcs

def proper_nouns(text): ## 3. Найти все имена собственные, кроме тех, которые стоят начале предложения.
    proper = re.findall('[а-яёa-z0-9] [А-ЯЁA-Z][а-яёa-z]+?[\s,.!\?:"\(\)\'»\n]' , text)
    for i in range(len(proper)):
        proper[i] = proper[i].split()[1]
        proper[i] = proper[i].strip('\s,.!\?:"\(\)\'»\n\t')
    return proper

def analytical_future(text): ## 4. Найти все конструкции типа "буд(у/ешь/ет/ут/ем) + инфинитив".
    future = re.findall(r'буд(?:е(?:шь|те?|м)|ут?) .+?(?:а|е|и)ть(?:ся)?', text, re.I)
    return future

def polysyllabic(text): ## 5. Найти все слова, которые состоят из 5 и более слогов.
    poly = re.findall('[\s,.!\?:"\(\)\'«\n ](?:[йцкнгшщзхфвпрлджчсмтб]*?[уеыаоюяиэ]){5,}[а-я]*?[\s,.!\?:"\(\)\'»\n]', text)
    for i in range(len(poly)):
        poly[i] = poly[i].strip('\s,.!\?:"\(\)\'«»\n\t ')
    return poly

def roman_num(text): ## 6. Найти все встречающиеся в тексте римские цифры.
    rawroman = re.findall('\sC?M*?C?D?L?C{,4}X?L?I?X{,4}I?V?I{,4}\s', text)
    roman = []
    for i in range(len(rawroman)):
        rawroman[i] = rawroman[i].strip('\s,.!\?:"\(\)\'«»\n\t ')
        if rawroman[i]:
            roman.append(rawroman[i])
    return roman

def main():
    with open('text.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
##    print(three_consonants(text))
##    print(startwith(text))
##    print(proper_nouns(text))
##    print(analytical_future(text))
##    print(polysyllabic(text))
##    print(roman_num(text))

if __name__ == '__main__':
    main()
