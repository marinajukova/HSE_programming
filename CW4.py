####задание на вложенные циклы
####вводятся две строки, выводятся попарно номера одинаковых символов
##word1 = input('Print anything. ')
##word2 = input('Print something else. ')
##for index1,letter1 in enumerate(word1):
##    for index2, letter2 in enumerate(word2):
##        if letter1 == letter2:
##            print(str(index1 + 1), str(index2 + 1))


####списки (в других языках называется "массивы")
##trashlist = ['c',2, 2.5,['a', 2, 2.6]]
##list1 = [] ## так задаётся пустой список
##
##list1.append('that trash you wanted to add to this list') ##так добавляется элемент в конец списка
##a = trashlist[3] ## a = ['a', 2, 2.6] вызов элемента из списка
##b = trashlist[3][1] ## b = 2 вызов элемента вложеннного списка
##
##words = 'Some words'
##list2 = list(words) ## преобразование строки в список, способ 1 list2 = ['S','o','m','e',' ','w','o','r','d','s']
##list2[4] = ' stupid ' ## list2 = ['S', 'o', 'm', 'e', ' stupid ', 'w', 'o', 'r', 'd', 's']
##
##words = 'Some words'
##list3 = words.split() ## преобразование строки в список, способ 2 list3 = ['Some', 'words'] - по умолчанию по пробелам и табуляции
##words = 'Something, something else, anything'
##list3 = words.split(',') ## list3 = ['Something', ' something else', ' anything']
##first_letter_of_second_word = list3[1][0]


#### Спрашивает слово, выводит все слова кроме слова "ёлка" в разных вариантах его написания
##words = input('Print something. ')
##while words != '':
##    list_of_words = words.split()
##    for word in list_of_words:
##        if word.lower() != 'ёлка' and word.lower() != 'елка' and word.lower() != 'йолка' and word.lower() != 'йолко':
##            print(word)
##    words = input('Print something else. ')


##list4 = [1, 2, 3, 4]
##for element in list4:
##    if element == 3:
##        element = 15 ## list4 = [1, 2, 3, 4]
##        
##for index, element in list4:
##    if element == 3:
##        list4[index] = 15 ## list4 = [1, 2, 15, 4]
##
#### разница между строками и массивами
##a = 'áaà'
##b = a
##b = 'bbb' ## a = 'áaà'
##list5 = ['á','a','à']
##list6 = list5
##list6[0] = 'b' ## list5 = ['b','a','à']

#### получить строку из массива
##words = ['May','I','ask?']
##string = ' '.join(words) ## string = 'May I ask?'
