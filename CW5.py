####Шифр Виженера Vigenère
####слово: ABCDAEB
####ключ: CDB(повторённое до длины слова)
####Алфавит в квадрате со сдвигом на 1 в каждой строке
####каждая следующая буква кодируется данной буквой из строки соответствующей букве ключа
####print(*массив) - печатать элементы массива через пробел
##
##alphabet = list('abcdefghijklmnopqrstuvwxyz')
##table = []
##
##for i in range(len(alphabet)):
##    table.append(alphabet[i:]+alphabet[:i])
##
##word = input('Print any English word: ')
##key = input('Print your key: ')
##
##if len(key)>=len(word):
##    key = key[:len(word)]
##else:
##    key = key * (len(word)//len(key)) + key[:len(word)%len(key)]
##
##cipher =''
##for i in range(len(word)):
##    j = alphabet.index(key[i]) ## индекс строки
##    k = alphabet.index(word[i]) ## индекс столбца
##    cipher += table[j][k]
##
##print(cipher)
##
##todecipher = input('Print the word you want to decipher: ')
##key = input('Print your key: ')
##
##if len(key)>=len(todecipher):
##    key = key[:len(todecipher)]
##else:
##    key = key * (len(todecipher)//len(key)) + key[:len(todecipher)%len(key)]
##    
##decipher =''
##for i in range(len(todecipher)):
##    j = alphabet.index(key[i]) ## индекс строки
##    k = table[j].index(todecipher[i]) ## индекс буквы в алфавите
##    decipher += alphabet[k]
##    
##print(decipher)

##поросячья латынь:
####    Если слово начинается на один или несколько согласных звуков, первые согласные перемещаются в конец слова и добавляется ay. Так ball («шар», «мяч») превращается в all-bay, button («пуговица», «кнопка») — в utton-bay, star («звезда») — в ar-stay, three («три») — в ee-thray, question («вопрос») — в estion-quay.
####Если слово начинается на гласный звук, в конце просто добавляется определённый слог, оканчивающийся на ay. Какой именно слог, зависит от конкретного «диалекта» поросячьей латыни: это могут быть слоги way, yay, hay, а чаще просто ay. Таким образом, a (неопределённый артикль) в зависимости от «диалекта» превращается в a-ay, a-way, a-yay или a-hay. Следует иметь в виду, что, напр. honest («честный») переводится как honest-ay, а не onest-hay, так как это слово начинается на согласную букву, но на гласный звук, первая буква h не произносится.
##
##consonants = 'qrtpsdfgklzxcvbnm'
##index = 0
##text = input('Print any text in English: ')
##text = text.split(' ')
##for i in range(len(text)):
##    if not text[i][0] in consonants:
##        text[i] += 'way'
##    else:
##        for letter in text[i]:
##            if not letter in consonants:
##                index = text[i].index(letter)
##        text[i] = text[i][index:]+ text[i][:index] + 'ay'
##print(*text)
