## Программа должна прочитать текст, создать частотный список слов в этом тексте, используя слова в качестве ключей словаря,
## а частотность в качестве значений. После этого нужно распечатать самое частотное слово в тексте.
## Найти среднее значение частотности слов в тексте и распечатать его.

def process(fname):
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    forms = text.split()
    for i in range(len(forms)):
        forms[i] = forms[i].strip('.,!?*()«»\'":][><')
    return forms


def freqlist(forms):
    freqs = {}
    for i in range(len(forms)):
        if forms[i] not in freqs:
            freqs[forms[i]] = 1
        else:
            freqs[forms[i]] +=1
    return freqs


def maxfreq(frequencies):
    maximumfreq = []
    for key in frequencies:
        if frequencies[key] == max(frequencies.values()):
            maximumfreq.append(key)
    return maximumfreq


def averagefreq(frequencies):
    total = 0
    for key in frequencies:
        total += frequencies[key]
    average = total/len(frequencies)
    return average


def main():
    forms = process('text.txt')
    frequencies = freqlist(forms)
    print(*maxfreq(frequencies), '- самое частотное слово в тексте.')
    print(averagefreq(frequencies), '- средняя частота слов в тексте.')

if __name__ == '__main__':
    main()
