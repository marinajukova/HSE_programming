##Вариант 3. Программа должна открывать файл с русским текстом в utf-8 и сообщать про него следующую информацию:
##во сколько раз слов длины 3 больше, чем слов длины 1 (если слов длины 1 нет вообще, программа должна об этом сообщить)

## !!! Программа работает только с utf-8 без BOM !!!

words = []
with open('text.txt','r', encoding = 'utf-8') as f:
    text = f.read()
    words_raw = text.split()
    words = []
    for i in range(len(words_raw)):
        words.extend(words_raw[i].split('\n'))

len3 = 0
len1 = 0
for word in words:
    if len(word) == 3:
        len3 += 1
    elif len(word) == 1:
        len1 += 1

if len1 == 0:
    print('В файле нет слов длины 1.')
elif len3 == 0:
    print('В файле нет слов длины 3.')
else:
    print('В файле в '+str(len3/len1)+' раз больше слов длины 3, чем слов длины 1.')
