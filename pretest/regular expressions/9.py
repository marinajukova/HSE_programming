## Замените все вхождения слова "кошка" во всех формах на слово "собака", а вхождения слова "собака" на слово "кошка".
## Если вы сначала замените всех "кошек" на "собак", то вы не сможете отличить "собак" - заменённых "кошек" от исходных "собак". Эту проблему нужно обойти.
## Решите возникающие проблемы: замена в словах типа "лукошка" и замена слова с большой буквы (Кошка) на слово с маленькой буквы (собака).
## замените также "кошачьи" на "собачьи" во всех формах, а "котенок" и "котята" на "щенок" и "щенята".
## Обратите внимание, что "который" и подобные слова не должны ни на что заменяться!

import re

def main():
    with open('cats.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
    mark_dogs = re.sub('([Сс]обак(?:а(?:х|ми?)?|и|е|у|о(?:й|ю))?)([\s,.!\?:"\(\)\'»\n\]\[-])', '<<<тут было слово \\1>>> \\2', text)
    catstodogs = re.sub('([\s,.!\?:"\(\)\'«\n-])коше?к(а(?:х|ми?)?|и|е|у|о(?:й|ю))?([\s,.!\?:"\(\)\'»\n-\]\[])', '\\1собак\\2\\3', mark_dogs)
    CatstoDogs = re.sub('([\s,.!\?:"\(\)\'«\n-])Коше?к(а(?:х|ми?)?|и|е|у|о(?:й|ю))?([\s,.!\?:"\(\)\'»\n-\]\[])', '\\1Собак\\2\\3', catstodogs)
    dogstocats = re.sub('<<<тут было слово собак(а(?:х|ми?)?|и|е|у|о(?:й|ю))>>>', 'кошк\\1', CatstoDogs)
    dogstocats2 = re.sub('<<<тут было слово собак>>>', 'кошек', dogstocats)
    DogstoCats = re.sub('<<<тут было слово Собак(а(?:х|ми?)?|и|е|у|о(?:й|ю))>>>', 'Кошк\\1', dogstocats2)
    DogstoCats2 = re.sub('<<<тут было слово Собак>>>', 'Кошек', DogstoCats)
    catishtodogish = re.sub('кошач(ь(?:и(?:ми?|х)?|е(?:му|го|й)|я|ю)?|ий)', 'собач\\1', DogstoCats2)
    CatishtoDogish = re.sub('Кошач(ь(?:и(?:ми?|х)?|е(?:му|го|й)|я|ю)?|ий)', 'Собач\\1', catishtodogish)
    kittenstopyppies = re.sub('котята','щенята', CatishtoDogish)
    KittenstoPyppies = re.sub('Котята','Щенята', kittenstopyppies)
    kittentopyppy = re.sub('кот(?:е|ё)н(ок|ку)','щен\\1', KittenstoPyppies)
    KittentoPyppy = re.sub('Кот(?:е|ё)н(ок|ку)','Щен\\1', kittentopyppy)
    print(KittentoPyppy)

if __name__ == '__main__':
    main()
