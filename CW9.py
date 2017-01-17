##dictionary = {} ## создали пустой словарь с именем dictionary, в который можно добавлять пары ключ:значение, ключи - строки или числа
##phones = {'alice':'898', 'bob':'891'}## создали с именем phones, в котором живут номера телефонов по именам
##print(phones['alice']) ## напечатает 898
##phones['bob'] = '888' ## меняет значение 'bob' на 888
##phones['john'] = '771' ## добавляет ключ 'john' со значением 771
##print(len(phones)) ## 3
##if 'bob' in phones: ##  проверяет есть ли ключ 'bob' и печатает его значение (нельзя дать значение от несуществующего ключа, алючи не могут повторяться)
##    print(phones['bob'])
##for key in phones: ## печатает ключ+':'+значение (неупорядоченно)
##    print(key+':'+phones[key])
##numbers = phones.values() ## массив значений
##names = phones.keys() ## массив ключей
##alphabetic_names = sorted(names) ## рассортирует массив по алфавиту, возрастанию и вернёт его
##sort(names) ## рассортирует массив по алфавиту, возрастанию (меняет массив)

#### Написать словарь, где ключи - страны, а значения - столицы (5-6 шт), и распечатать в цикле ключ:значение
##
##capitals = {'Greece':'Athens', 'Russia':'Moscow', 'UK':'London', 'USA':'Washington', 'Australia':'Canberra'}
##for key in capitals:
##   print(key+':'+capitals[key])

#### Написать функцию capital, если страна есть в словаре - возвращает столицу, если нет - говорит, что нет
##def capital():
##    cap = input('Type any country: ')
##    capitals = {'Greece':'Athens', 'Russia':'Moscow', 'UK':'London', 'USA':'Washington', 'Australia':'Canberra'}
##    if cap in capitals:
##        return capitals[cap]
##    else:
##        return 'I am sorry, but there is no such country in my list. '

#### Написать функцию revert(dictionary), которая меняет ключи и значения местами
##def revert(dictionary):
##    reverted = {}
##    for key in dictionary:
##        reverted[dictionary[key]] = key
##    return reverted
#### Написать функцию delete_doubles(dictionary), озвращающую полученный на вход словарь без ключей с повторяющимися значениями
##def delete_doubles(dictionary):
##    return(revert(revert(dictionary)))

#### Написать функцию delete_doubles(dictionary), озвращающую полученный на вход словарь без ключей с повторяющимися значениями, не используя revert(dictionary)
##def delete_doubles(dictionary):
##    clear = {}
##    seen = []
##    for key in dictionary:
##        if dictionary[key] not in seen:
##            clear[key] = dictionary[key]
##            seen.append(dictionary[key])
##    return clear

#### Написать функцию freqlist(text), которая возвращает частотный словарь текста
##def freqlist(text):
##    freqs = {}
##    text = text.lower()
##    forms = text.split()
##    for i in range(len(forms)):
##        forms[i] = forms[i].strip('.,!?*()«»\'"')
##    for i in range(len(forms)):
##        if forms[i] not in freqs:
##            freqs[forms[i]] = 1
##        else:
##            freqs[forms[i]] +=1
##    return freqs
##
#### Написать функцию maxfreq(fname), наиболее частотные слова из текста из файла
##def maxfreq(fname):
##    forms = []
##    with open (fname, 'r', encoding = 'utf-8') as f:
##        text = f.read()
##    frequencies = freqlist(text)
##    maximumfreq = []
##    for key in frequencies:
##        if frequencies[key] == max(frequencies.values()):
##            maximumfreq.append(key)
##    print(max(frequencies.values()))
##    return maximumfreq
##
#### Написать функцию minfreq(fname), наиболее частотные слова из текста из файла
##def minfreq(fname):
##    forms = []
##    with open (fname, 'r', encoding = 'utf-8') as f:
##        text = f.read()
##    frequencies = freqlist(text)
##    minimumfreq = []
##    for key in frequencies:
##        if frequencies[key] == min(frequencies.values()):
##            minimumfreq.append(key)
##    print(min(frequencies.values()))
##    return minimumfreq
