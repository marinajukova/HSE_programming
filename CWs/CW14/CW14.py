import re
import os
from math import log

##предобработка
def open_words(fname):
    forms = []
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    punct = '[.,?!|:;*№\"\'—@#$%()«»…€&’”-]'
    text = re.sub(punct, '', text)
    text = re.sub('[\n\t]', ' ', text)
    forms = text.split()
##    for i in range(len(forms)):
##        forms[i] = forms[i].strip('.,?*()«»')
    return forms


##частотный словарь
def make_freq(arr):
    d = {}
    for el in arr:
        try:
            d[el] += 1
        except KeyError:
            d[el] = 1
    return d


##сделать биграммы
def make_bigrams(arr):
    bigrams = []
    for i in range(len(arr)-1):
        bigr = arr[i] + ' ' + arr[i+1]
        bigrams.append(bigr)
    return bigrams


##словарь pmi
def count_pmi(x, y):
    try:
        p_x = word_freq[x]/len(words)
    except KeyError:
        p_x = 0
    try:
        p_y = word_freq[x]/len(words)
    except KeyError:
        p_y = 0
    try:
        bigr = x + ' ' + y
        p_xy = bigrams_freq[bigr]/len(bigrams)
    except KeyError:
        p_xy = 0
    try:
        pmi = log(p_xy/(p_x*p_y))
    except ZeroDivisionError:
        pmi = 0
    return pmi

##посчитать pmi для всех bigram
def calculate_pmi():
    pmis = {}
    for bigr in bigrams:
        x, y = bigr.split()
        pmi = count_pmi(x, y)
        pmis[bigr] = pmi
    return pmis


####посчитать pmi для всех bigram
##def calculate_pmi():
##    pmis = {}
##    for bigr in bigrams:
##        x, y = bigr.split()
##        pmi = count_pmi(x, y)
##        pmis[bigr] = pmi
##    return pmis

##words = open_words(fname)   
##word_freq = make_freq(words)
##bigrams = make_bigrams(words)
##bigrams_freq = make_freq(bigrams)
##pmi_dict = calculate_pmi()
##    i = 0
##    for el in sorted(pmi_dict, key = lambda m: -pmi_dict[m]): ## key - значение, по которому сортируют
##        if i > 100:
##            break
##        print(el, pmi_dict[el])
##        i += 1

##посчитать pmi для всех категорий
def calculate_pmi_cats(word, cathegory):
    p_word = freq_all[word]/len(words_all)
    p_cat = 1/3
    if cathegory == 'anek':
        d = freq_anek
        w = len(corpus_anek_words)
    elif cathegory == 'izvest':
        d = freq_izvest
        w = len(corpus_izvest_words)
    elif cathegory == 'teh':
        d = freq_teh
        w = len(corpus_teh_words)
    p_word_cat = d[word]/w
    pmi = log(p_word_cat/(p_word*p_cat))
    return pmi

def main():
    corpus_anek_words = []
    corpus_izvest_words = []
    corpus_teh_words = []
    for root, dirs, files in os.walk('texts'):
        if 'anekdots' in root:
            for f in files:
                corpus_anek_words += open_words(os.path.join(root, f))
        if 'teh_mol' in root:
            for f in files:
                corpus_teh_words += open_words(os.path.join(root, f))
        if 'izvest' in root:
            for f in files:
                corpus_izvest_words += open_words(os.path.join(root, f))
    words =   corpus_anek_words + corpus_teh_words + corpus_izvest_words
    freq_anek = make_freq(corpus_anek_words)
    freq_izvest = make_freq(corpus_izvest_words)
    freq_teh = make_freq(corpus_teh_words)
    freq_all = make_freq(words)
    words_cathegory_dict = {}
    for w in words:
        i = 0
        try:
            if i < 100:
                pmi_anek = calculate_pmi_cats(w, 'anek')
                pmi_cats(w, 'anek')
                pmi_izvest = calculate_pmi_cats(w, 'izvest')
                pmi_teh = calculate_pmi_cats(w, 'teh')
                pmi_max = max(pmi_anek, pmi_izvest, pmi_teh)
                if pmi_max == pmi_anek:
                    words_cathegory_dict[w] = 'anek'
                if pmi_max == pmi_teh:
                    words_cathegory_dict[w] = 'teh'
                if pmi_max == pmi_anek:
                    words_cathegory_dict[w] = 'teh'
            i += 1
        except KeyError:
            pass
    print(words_cathegory_dict)



if __name__ == '__main__':
    main()
