## 3. Спрашивает у пользователя слово
## и выводит на экран все буквы этого слова задом наперёд, пропуская буквы "з" и "я".

##word = input('Введите слово в русской раскладке.')
##for index in range(len(word)):
##    if word[len(word) - index - 1] != 'з' and word[len(word) - index - 1] != 'я':
##        print(word[len(word) - index - 1])
        
word = input('Введите слово в русской раскладке.')
index = 0
while index < len(word):
    index += 1
    if word[len(word) - index] != 'з' and word[len(word) - index] != 'я':
        print(word[len(word) - index])

