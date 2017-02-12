## Пользователь вводит номер своего мобильного телефона.
## Программа должна проверить, соответствует ли введенный номер шаблону +7 (ХХХ) ХХХ-ХХ-ХХ и сообщить, совпал ли номер с шаблоном или нет.
## Можно усовершенствовать программу, чтобы она ещё и сообщала, какой у пользователя мобильный оператор.

import re

def main():
    given = input('Введите свой телефонный номер: ')
    right = re.search('\+7 \([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}', given)
    if right:
        print('Введённый номер совпадает с шаблоном +7 (ХХХ) ХХХ-ХХ-ХХ.')
        if re.search('\(9(?:2|3)', given):
            print('Это Мегафон.')
        elif re.search('\(9(?:1|8)', given):
            print('Это МТС.')
        elif re.search('\(96', given):
            print('Это Билайн.')
        else:
            print('Я не могу точно сказать, какой это оператор.')
    else:
        print('Введённый номер не совпадает с шаблоном +7 (ХХХ) ХХХ-ХХ-ХХ.')
        if re.search('\(9(?:2|3)', given) or re.search('\+7 ?9(?:2|3)', given) or re.match('8 ?9(?:2|3)', given):
            print('Это Мегафон.')
        elif re.search('\(9(?:1|8)', given) or re.search('\+7 ?9(?:1|8)', given) or re.match('8 ?9(?:1|8)', given):
            print('Это МТС.')
        elif re.search('\(96', given) or re.search('\+7 ?96', given) or re.match('8 ?96', given):
            print('Это Билайн.')
        else:
            print('Я не могу точно сказать, какой это оператор.')

if __name__ == '__main__':
    main()