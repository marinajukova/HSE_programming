##3. Текст должен состоять из 5 предложений разных типов
##(утвердительные, вопросительные, отрицательные, условные, побудительные)на русском языке.
##Типы предложений должны выводиться в случайном порядке.

import random

def nom_noun():
    with open('nomnouns.txt','r', encoding = 'utf-8') as f:
        nomnouns = f.read().split('\n')      
    return random.choice(nomnouns)

def acc_noun():
    with open('accnouns.txt','r', encoding = 'utf-8') as f:
        accnouns = f.read().split('\n')
    return random.choice(accnouns)

def adverb():
    with open('adverbs.txt','r', encoding = 'utf-8') as f:
        adverbs = f.read().split('\n')
    return random.choice(adverbs)

def intensifier(adv):
    with open('intensifiers.txt','r', encoding = 'utf-8') as f:
        intensifiers = f.read().split('\n')
    return random.choice(intensifiers) + ' ' + adv

def verb_of_thought(subj):
    with open('thoughtverbs.txt','r', encoding = 'utf-8') as f:
        thoughtverbs = f.read().split('\n')
    return subj + ' ' + random.choice(thoughtverbs) + ', что ' + trans_verb(nom_noun(), acc_noun()) + '.'

def trans_verb(subj, obj):
    with open('transverbs.txt','r', encoding = 'utf-8') as f:
        transverbs = f.read().split('\n')
    return subj + ' ' + intensifier(adverb()) + ' ' + random.choice(transverbs)+ ' ' + obj

def trans_verb_negative(subj, obj):
    with open('transverbs.txt','r', encoding = 'utf-8') as f:
        transverbs = f.read().split('\n')
    negative_sentences = [subj + ' не ' + intensifier(adverb()) + ' ' + random.choice(transverbs)+ ' ' + obj, subj + ' ' + intensifier(adverb()) + ' не ' + random.choice(transverbs)+ ' ' + obj]
    return random.choice(negative_sentences)

def verb_of_thought_negative(subj, obj):
    with open('thoughtverbs.txt','r', encoding = 'utf-8') as f:
        thoughtverbs = f.read().split('\n')
    return subj + ' не ' + random.choice(thoughtverbs) + ', что ' + trans_verb(nom_noun(), acc_noun()) + '.'

def positive():
    positive_sentences = [trans_verb(nom_noun(), acc_noun()) + '.', verb_of_thought(nom_noun())]
    return random.choice(positive_sentences)

def question():
    questions = ['зачем ' + trans_verb(nom_noun(), acc_noun()) + '?', 'почему ' + verb_of_thought(nom_noun())]
    return random.choice(questions)

def negative():
    negative_sentences = [verb_of_thought_negative(nom_noun(), acc_noun()), trans_verb_negative(nom_noun(), acc_noun())]
    return random.choice(negative_sentences)

def conditional():
    with open('transverbs.txt','r', encoding = 'utf-8') as f:
        transverbs = f.read().split('\n')
    conditional_sentences = ['если ' + positive().strip('.') + ', то ' + nom_noun() + ' ' + random.choice(transverbs)+ ' ' + acc_noun(), 'если ' + positive().strip('.') + ', то ' + nom_noun() + ' не ' + random.choice(transverbs)+ ' ' + acc_noun(), 'если ' + negative().strip('.') + ', то ' + nom_noun() + ' ' + random.choice(transverbs)+ ' ' + acc_noun(), 'если ' + negative().strip('.') + ', то ' + nom_noun() + ' не ' + random.choice(transverbs)+ ' ' + acc_noun()]
    return random.choice(conditional_sentences)

def imperative():
    with open('imperatives.txt','r', encoding = 'utf-8') as f:
        imperatives = f.read().split('\n')
    imperative_sentences = ['пусть ' + positive(), 'пусть ' + negative(), 'пусть ' + conditional(), random.choice(imperatives) + ' ' + acc_noun()]
    return random.choice(imperative_sentences)

def main():
    sentences = [positive(), question(), negative(), conditional(), imperative()]
    random.shuffle(sentences)
    for i in range(5):
        print(sentences[i].capitalize())
    
if __name__ == '__main__':
    main()    
