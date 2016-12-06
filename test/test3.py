##3. (10 баллов) Программа должна спрашивать у пользователя слова, пока тот не введёт пустое слово.
##После этого она должна для каждого слова распечатать а) морфологическую информацию о слове и б)ipm слова. Если слово не встретилось в словаре, то нужно вывести сообщение о том, что слово не нашлось.

words = []
with open('words.txt','r', encoding = 'utf-8') as f:
    text = f.read()
    words = text.split('\n')

words1 = []
word = input('Print any russian word. ')
while word:
    words1.append(word)
    word = input('Print any russian word. ')

for i in range(len(words1)):
    check = 0 
    for x in range(len(words)):
        if words[x].count('|') == 2:
            word, gram, ipmi = words[x].split('|')
            if words1[i] == word.strip(' '):
                print('grammar:', gram.strip(' ')+',' , 'ipm =', float(ipmi))
                check = 1
    if check == 0:
            print('This word was not find in the dictionary.')
