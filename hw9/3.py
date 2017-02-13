##3. В этом домашнем задании программа должна открывать файл с русским текстом в кодировке UTF-8 и
##распечатывать из него по одному разу все встретившиеся в нём формы глагола "программировать".
##В формы глагола включаются деепричастия, причастия и формы на -ся и не включаются видовые пары
##(тем более что не у всех из перечисленных глаголов они имеются).
##И особое внимание стоит уделить тому, чтобы программа ничего, кроме форм этих глаголов, не распознавала.
import re


def match_verb_forms(line):
    infinitive = re.match(r'программировать(ся)?', line, re.I)
    future = re.match(r'буд(е(шь|те?|м)|ут?) программировать', line, re.I)
    present = re.match(r'программиру(ю|(е(те?|м|шь)))', line, re.I)
    past = re.match(r'программировал(а|и)?', line, re.I)
    past_participle = re.match(r'программированн(ая|о(е|й|му?|го)|ы(й|е|ми?|х))', line, re.I)
    present_participle = re.match(r'программируем(ая|о(е|й|му?|го)|ы(й|е|ми?|х))', line, re.I)
    transgressive_active = re.match(r'программируя', line, re.I)
    transgressive_passive_past = re.match(r'будучи программированн(ая|о(е|й|му?|го)|ы(й|е|ми?|х))', line, re.I)
    transgressive_passive_present = re.match(r'будучи программируем(ая|о(е|й|му?|го)|ы(й|е|ми?|х))', line, re.I)
    if infinitive and not future:
        match = infinitive
    elif future:
        match = future
    elif present:
        match = present
    elif past:
        match = past
    elif past_participle:
        match = past_participle
    elif present_participle:
        match = present_participle
    elif transgressive_active:
        match = transgressive_active
    elif transgressive_passive_past and not past_participle:
        match = transgressive_passive_past
    elif transgressive_passive_present and not present_participle:
        match = transgressive_passive_present
    else:
        match = None
    return match

def open_forms(fname):
    forms = []
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    forms = text.split()
    for i in range(len(forms)):
        forms[i] = forms[i].strip('.,?*()«»')
    return forms

def main():
    matches = []
    forms = open_forms('test.txt')
    for i in range(len(forms)-1):
        if i < len(forms):
            if match_verb_forms(forms[i] +' '+ forms[i+1]):
                if match_verb_forms(forms[i] +' '+ forms[i+1]).group() not in matches:
                    matches.append(match_verb_forms(forms[i] +' '+ forms[i+1]).group())
        else:
            if match_verb_forms(forms[i]):
                if match_verb_forms(forms[i]).group()not in matches:
                    matches.append(match_verb_forms(forms[i]).group())
    print(*matches)
            
    
if __name__ == '__main__':
    main()
