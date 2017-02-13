## Написать программу, которая спрашивает у пользователя, какие у него
##    имя,
##    фамилия,
##    возраст,
##    любимая еда,
##    музыкальная группа,
##    заветная мечта.
## Результаты программа должна складывать в словарь, в котором ключи - имена и фамилии пользователей, значения - все остальное.
## Программа должна спрашивать эту информацию у 7 пользователей.
## Потом она должна загадывать вам мечту, или мечту и еду, или музыкальную группу, или музыкальную группу и еду
##(выбирая, что именно загадать, случайным образом) и предлагать угадать, что это был за пользователь.

import random


def ask():
    user_info = []
    name = input('Как Вас зовут? ')
    surname = input('Какая у Вас фамилия? ')
    age = input('Сколько Вам лет? ')
    food = input('Какая у Вас любимая еда? ')
    musician = input('Какая у Вас любимая музыкальная группа? ')
    dream = input('Какая у Вас заветная мечта? ')
    user_info.append(name+' '+surname)
    user_info.append([age, food, musician, dream])
    return user_info


def guess(database_dictionary):
    person = random.choice(list(database_dictionary.keys()))
    clue = random.choice(['его/её мечта: '+database_dictionary[person][3], 'его/её любимая музыкальная группа: '+database_dictionary[person][2], 'его/её мечта: '+database_dictionary[person][3]+'\nего/её любимая еда: '+database_dictionary[person][1], 'его/её любимая музыкальная группа: '+database_dictionary[person][2]+'\nего/её любимая еда: '+database_dictionary[person][1]])
    guess = input('Угадайте, кто это (имя и фамилию)? Подсказка: '+clue+' ')
    if guess == person:
        return 'Правильно!'
    else:
        return 'Нет, неправильно, это - '+person


def main():
    database = {}
    i = 0
    while i < 7:
        answer = ask()
        i += 1
        database[answer[0]] = answer[1]
    print(guess(database))


if __name__ == '__main__':
    main()
