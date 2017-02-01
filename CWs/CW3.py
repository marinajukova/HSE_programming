#### про enumerate
##s = input()
##for index, letter in enumerate(s):
##    print(index,':',letter)
#### то же что и
##for i in range(len(s)):
##    print (i,':', s[i])

#### номер начала каждого слова
##st = input()
##for index, symbol in enumerate(st):
##    if symbol == ' ' and index != len(st)-1 or index == 0 or index == len(st):
##       print(index)

#### вводится имя и слово вывести имя без первой и последней букв
##sname = input()
##for index in range(len(sname)):
##    if sname[index] == ' ':
##        print(sname[(index+2):len(sname)-1])


#### про replace
####вводится имя и строка вывести строку без первых двух букв имени
##name = input("What's your name?")
##deal = input("How are you?")
##cutdeal = deal.replace(name[0], '')
##cutdeal = cutdeal.replace(name[1], '')
##print(cutdeal)
#### то же что и
##name = input("What's your name?")
##deal = input("How are you?")
##for index, symbol in enumerate(deal):
##    if symbol == name[0] or symbol == name[1]:
##        cutdeal = deal[:index-1] + deal[index+1:]
##print(cutdeal)

####про цикл while
##i = 1
##s = 0
##while s<500:
##    s+=i
##    i+=1
##print(i)
##
##s = input()
##while s: ## пока s - непустая строка
##    print(s.lower) ## все буквы в нижнем регистре

####распечатыывать корень числа пока пользователь не введёт пустую строку, прекращается при отрицательном числе
##n = input("Введите число. ")
##while n:
##    n = int(n)
##    if n<0:
##        break
##    print (n**1/2)
##    n = input("Введите число. ")

####распечатыывать корень числа пока пользователь не введёт пустую строку, просит положительное число при отрицательном числе
##n = input("Введите число. ")
##while n:
##    n = int(n)
##    if n<0:
##        n = input("Введите лучше положительное число. ")
##        continue
##    print (n**(1/2))
##    n = input("Введите число. ")

####пользователь вводит числа до пустой строки выводится сумма только тех чисел, которые больше 100 если введено число кратное 500 то прекратить спрашивать числа
##n = input("Введите число. ")
##m = 0
##while n:
##    n = int(n)
##    if n%500 == 0:
##        break
##    if n>100:
##        sum += n
##        n = input("Введите число. ")
##        continue
##    n = input("Введите число. ")
##print(sum)
