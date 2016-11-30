##1. Программа спрашивает у пользователя:
##    1. Имя
##    2. Возраст
##    3. Любимый цвет
##    4. Любимый муз. исполнитель
##    5. Мечта
## Всю информацию записываем в файл information.txt:
##    Елизавета Кузьменко
##    200
##    голубой
##    Филипп Киркоров
##    Полететь на Марс
##
##2. Программа спрашивает у вас:
##    "Как зовут вашего соседа?"
##    Лиза
##    "Нет, неправильно, плохо знаешь соседа. Его зовут Елизавета Кузьменко"
##    и так далее

with open('information.txt', 'w', encoding = 'utf-8') as n:
    name = input('Как Вас зовут? ')
    n.write(name+'\n')
    age = input('Сколько Вам лет? ')
    n.write(str(age)+'\n')
    color = input('Какой у Вас любимый цвет? ')
    n.write(color+'\n')
    musician = input('Какой у Вас любимый исполнитель? ')
    n.write(musician+'\n')
    dream = input('Какая у Вас мечта? ')
    n.write(dream+'\n')

with open('information about Mary.txt','r', encoding = 'utf-8') as f:
    info = f.readlines()
    for line in range(len(info)):
        info[line] = info[line].strip()
    response = input('Как Вашего соседа зовут? ')
    if response == info[0]:
        print('Правильно!')
    else:
        print('Нет, его зовут '+info[0]+'.')
    response = input('Сколько Вашему соседу лет? ')
    if str(response) == info[1]:
        print('Правильно!')
    else:
        print('Нет, ему '+info[1]+' лет.')
    response = input('Какой у Вашего соседа любимый цвет?')
    if response == info[2]:
        print('Правильно!')
    else:
        print('Нет, его любимый цвет - '+info[2]+'.')
    response = input('Какой у Вашего соседа любимый исполнитель?')
    if response == info[3]:
        print('Правильно!')
    else:
        print('Нет, его любимый исполнитель - '+info[3]+'.')
    response = input('Какая у Вашего соседа мечта?')
    if response == info[4]:
        print('Правильно!')
    else:
        print('Нет, его мечта - '+info[4]+'.')
