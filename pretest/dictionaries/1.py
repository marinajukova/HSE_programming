## Программа должна прочитать текст, создать частотный список слов в этом тексте, используя слова в качестве ключей словаря,
## а частотность в качестве значений. После этого нужно распечатать самое частотное слово в тексте.
## Найти среднее значение частотности слов в тексте и распечатать его.

def freqlist(text):
    freqs = {}
    text = text.lower()
    forms = text.split()
    for i in range(len(forms)):
        forms[i] = forms[i].strip('.,!?*()«»\'"')
    for i in range(len(forms)):
        if forms[i] not in freqs:
            freqs[forms[i]] = 1
        else:
            freqs[forms[i]] +=1
    return freqs

def maxfreq(text):
    frequencies = freqlist(text)
    maximumfreq = []
    for key in frequencies:
        if frequencies[key] == max(frequencies.values()):
            maximumfreq.append(key)
    return maximumfreq

def averagefreq(text):
    frequencies = freqlist(text)
    total = 0
    for key in frequencies:
        total += frequencies[key]
    average = total/len(frequencies)
    return average

def main():
    with open ('text.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
    print(*maxfreq(text), '- самое частотное слово в тексте.')
    print(averagefreq(text), '- средняя частота слов в тексте.')

if __name__ == '__main__':
    main()
