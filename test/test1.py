## 1. Программа должна открыть частотный словарь в кодировке UTF-8 и корректно вывести на экран только строчки с союзами.
words = []
with open('words.txt','r', encoding = 'utf-8') as f:
    text = f.read()
    words = text.split('\n')

for i in range(len(words)):
    if ' союз ' in words[i]:
        print(words[i])
