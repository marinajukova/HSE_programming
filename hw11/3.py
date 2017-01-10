##3. Программа с помощью отдельной функции принимает от пользователя название файла с английским текстом, читает этот файл и сообщает:
##- выводит сколько в тексте существительных с суффиксом -hood,
##- выводит какое существительное имеет минимальную частотность
##- выводит слова, от которых эти существительные образованы (например, если нашлось childhood, то нужно напечатать child).

def opentext(fname):
    forms = []
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    forms = text.split()
    for i in range(len(forms)):
        forms[i] = forms[i].strip('.,!?*()«»\'"')
    return forms


def adj_hood(fname):
    words = opentext(fname)
    hoods = []
    for i in range(len(words)):
        if len(words[i])>4:
          if words[i][-1] == 'd':
              if words[i][-2] == 'o':
                  if words[i][-3] == 'o':
                     if words[i][-4] == 'h':
                         if words[i] not in hoods:
                             hoods.append(words[i])
    return hoods

def count_frequency(fname, word):
    words = opentext(fname)
    word_freq = 0
    for i in range(len(words)):
        if words[i] == word:
            word_freq += 1
    return word_freq

def main():
    fname = input('Введите имя файла: ')
    hoods = adj_hood(fname)
    print('В тексте встретилось', len(hoods), 'прилагательных с суффиксом -hood.')
    freq = []
    for i in range(len(hoods)):
        freq.append(count_frequency(fname, hoods[i]))
    min_freq = []
    for i in range(len(hoods)):
        if freq[i] == min(freq):
            min_freq.append(hoods[i])
    print('Самые редкие прилагательные с суффиксом -hood: ', ', '.join(min_freq))
    roots = []
    for i in range(len(hoods)):
        roots.append(hoods[i][0:-4])
    print('Корни прилагательных с суффиксом -hood: ', ', '.join(roots))
    
if __name__ == '__main__':
    main()
