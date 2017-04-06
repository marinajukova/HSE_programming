##csv - comma separated values
##tsv - tab separated values \t cells = ilne.split('\t')
##BOM Byte On Mark в начале файла
## cp1251 - кодировка винды
## utf-8 - кодировка для настоящих прогеров

#### это про csv
##import csv
##
### читаем csv
##with open('text.csv', 'r', encoding='utf-8') as f:
##    text = csv.reader(f, delimiter=',')
##    header = next(text) # если у вас есть заголовочная строка, 
##    # можно её сложить в отдельную переменную, чтобы не мешалась.
##    for row in text:
##        print(row)
##      
#### пишем csv
##numbers = [[x, x**2, x**3] for x in range(10)]
##with open('out.csv', 'w', encoding='utf-8') as n:
##    text = csv.writer(n, delimiter=',')
##    header = ['number', 'square', 'cube'] # это будет заголовок
##    text.writerow(header)
##    for row in numbers:
##        text.writerow(row)

## регулярные выражения
## . - любой символ, кроме конца строки, кроме \. [.] - это точки
## [а-я] - любой символ от а до я, [\-], [-] просто "-", [^a-z] - только не эта группа символов
## Квантификаторы:
##    * - повторение предыдущего символа, втч 0,
##    + - повторение предыдущего символа больше 0 раз,
##    ? - предыдущего символа может не быть (0 или 1 раз)
## ограничение жадности квантификатора: по умолчанию ест максимально длинное соотвествие,
## знак ? после квантификатора ограничивает жадность - будет есть более короткий кусок текста
## () - группировка, (|) - или

##import re
##
##with open ('test.txt', 'r', encoding = 'utf-8') as f:
##    text = f.read()
##reg = '([a-z.]+)@([a-z]+)\.com'
##r = re.search(reg, text) ## тип данных - не строка, а объект, ищет только первое вхождение
##if r:
##    gmail = r.group() ## группа всё вместе
##    username = r.group(1)
##    domain = r.group(2)
##    print('email found')
##    
##all_matches = re.findall(reg, text) ## тип данных - массив, в котором лежат все вхождения, рассортированные по группам в кортежах
#### если групп нет, это будет массив строк, к которому можно применить len(all_matches), его можно склеить с помощью ' '.join()
#### [('username';'domain'), ('username1';'domain1')]
#### скобки могут быть _незапоминающей_ группой: (?: ) - незапоминающая группа


import re

def main():
    with open ('china space programm.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
    reg = '«[А-ЯЁа-яё]+?-[1-9]+»'
    all_matches = re.findall(reg, text)
    pure_names =[]
    for i in range(len(all_matches)):
        if re.sub(r'-[1-9]+', '', all_matches[i]) not in pure_names:
            pure_names.append(re.sub(r'-[1-9]+', '', all_matches[i]))
    all_matches += pure_names
    print(all_matches)
    
if __name__ == '__main__':
    main()
