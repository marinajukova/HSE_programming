##nouns = ['a', 'a', 'a']
##print(*nouns, sep = ', ') ## Печатает массив через разделитель sep = ', '

#### пределяет простое ли число больше 2
##def prime(number): ## определение функции с именем prime и одним аргументом number
##    divs = range(2, number-1)
##    for d in divs:
##        if number % d == 0:
##            return False ## функция вернула False
##    return True ## функция вернула True
##up = int(input('Введите целое число.'))
##if up < 3:
##    'Число слишком маленькое'
##else:
##    for i in range(2, up):
##        if prime(i):
##            print(i)

#### определяет максимум из 2 чисел
##def maximum(a, b):
##    if a > b:
##        return a
##    elif b < a:
##        return b
##    else:
##        return a, b

#### определяет максимум из n чисел
##def maximum(*a): ## неизвестно сколько аргументов, всех называем a
##    return(max(a))

##def maximum(a, b, c, d = 10, e = 16): ## d по умолчанию = 10, e по умолчанию = 16
##    return max(a, b, c, d, e)
##print(maximum(4, 4, 2, e = 18)) ## e = 18


## функция от x1 y1 x2 y2 надо почитать длинну отрезка, задаваемой этими точками
##import maths ## импортирует модуль maths
##m = mats.sqrt(2) ## вызывает из модуля maths функцию sqrt (квадратный корень) и извлекает его из 2
##import sqrt from maths ## импортирует из модуля maths функцию sqrt
##import sqrt from maths as square_root ## Импортировать из maths функцию sqrt под названием square_root

####программа спрашивает у пользователя координаты 2 точек и ищет расстояние между ними
##def length(x1, y1, x2, y2):
##    return(((x1-x2)**2+(y1-y2)**2)**(1/2))
##def main(): ## сюда надо класть тело кода
##    x1 = float(input('Введите координату x первой точки'))
##    y1 = float(input('Введите координату y первой точки'))
##    x2 = float(input('Введите координату x второй точки'))
##    y2 = float(input('Введите координату y второй точки'))
##    print(length(x1, y1, x2, y2))
##if __name__ == '__main__': ## запускает функцию main
##    main()
  
