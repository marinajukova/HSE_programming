## Метрика tf - idf
## tf - term frequency = число вхождений этого слова в этом тексте - не работает для маленького текста
## idf - inverted document frequency = число текстов/число текстов с этим словом
## - не работает для очень большого текста (корпуса), чем больше коллекция, тем лучше работает
## 1. count tf
## 2. count idf
## 3. count tf-idf for all words in all texts
## 4. 5 minimal are key words

import os, codecs
from math import log

def preprocess(text):
    punct = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]'
    tabs = '\t\n'
    text_wo_punct = re.sub(punct, '', text.lower())
    text_wo_punct = re.sub(tabs, '', text_wo_punct)
    words = text_wo_punct.strip().split()
    return words


def count_tf(word, text):
    n = text.count(word)
    return n/len(text)


def count_df(word, texts):
##    i = 0
##    for text in texts:
##        if word in text:
##            i +=1
    i = [True for text in texts if word in text]
    df = len(i)
    return df


def count_idf(word, texts):
    df = count_df(word, texts)
    try:
        idf = len(texts)/df
    except ZeroDivisionError:
        return 0
    return idf


def count_tfidf(word, text, texts):
    tf = count_tf(word, text)
    idf = count_idf(word, texts)
    tfidf = log(tf, 10) * log(idf, 10)
    return tfidf


def extract_textS_from_folder(path):
    texts = []
    for root, dirs, files in os.walk(path):
        for f in files:
            with open(os.path.join(root, f) , "r", encoding = 'utf-8') as t:
                content = t.read
            text = preprocess(content)
            texts.append(text)
    return texts


def keywords(text, texts):
    keywords = {}
    dic_tfidf = {}
    for word in text:
        if word in dic_tfidf:
            continue
        tfidf = count_tfidf(word, text, texts)
        dic_tfidf[word] = tfidf
    i = 0
    for el in sorted(dic_tfidf, key = lambda x: dic_tfidf(x)):
        if i > 5:
            break
        else:
            i += 1
            keywords[el] = dic_tfidf[el]
    return keywords
    

def main():
    texts = extract_text_from_folder('wikipedia')
    for t in texts:
        kwords = keywords(t, texts)
        for key in kwords:
            print(key, kwords[key])


if __name__ == "__main__":
    main()
