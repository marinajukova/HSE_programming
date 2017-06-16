## Метрика tf - idf
## tf - term frequency = число вхождений этого слова в этом тексте - не работает для маленького текста
## idf - inverted document frequency = число текстов/число текстов с этим словом
## - не работает для очень большого текста (корпуса), чем больше коллекция, тем лучше работает

import os
import re
from math import log


def preprocessing(text): # функция предобработки текста
    punct = '[.,_!«»?&@"$\/\\[\]\(\):;%#^%&\'—]'
    tabs = '\n\t\s'
    num = '[0-9]'
    text_wo_punct = re.sub(punct, '', text.lower()) # удаляем пунктуацию, приводим в нижний регистр
    text_wo_punct = re.sub(tabs, ' ', text_wo_punct)
    text_wo_punct = re.sub(num, '', text_wo_punct)
    words = text_wo_punct.strip().split() # делим по пробелам
    return words

def count_tf(word, text):
    i = 0
    for w in text:
        if w == word:
            i += 1
    #i = text.count(word)
    tf = i / len(text)
    return tf


def count_df(word, texts):
    i = 0
    #for text in texts:
    #    for w in text:
    #        if w == word:
    #            i += 1
    #            break
    i = [1 for text in texts if word in text]
    df = sum(i)
    return df


def count_idf(word, texts):
    df = count_df(word, texts)
    idf = len(texts)/ (1 + df)
    return idf


def count_tfidf(word, text, texts):
    tf = count_tf(word, text)
    idf = count_idf(word, texts)
    tfidf = log(tf, 10) * log(idf, 10)
    return tfidf


def keywords(text, texts):
    dic_tfidf = {}
    kwords = {}
    for word in text:
        if word in dic_tfidf:
            continue
        tfidf = count_tfidf(word, text, texts)
        dic_tfidf[word] = tfidf
    i = 0
    for el in sorted(dic_tfidf, key=lambda x: dic_tfidf[x]):
        if i > 5:
            break
        else:
            i += 1
            kwords[el] = dic_tfidf[el]
    return kwords
    

def main():
    texts = {}
    for root, dirs, files in os.walk('wikipedia'):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='utf-8') as t:
                content = t.read()
                text = preprocessing(content)
                texts[f] = text
    raw_texts = list(texts.values())
    for t in texts:
        print('\nИзвлекаем ключевые слова для текста "{}"'.format(t.split('.')[0]))
        kwords = keywords(texts[t], raw_texts)
        for key in kwords:
            print (key, kwords[key])

if __name__ == '__main__':
    main()
