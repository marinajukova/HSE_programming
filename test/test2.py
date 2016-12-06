##2. (8 баллов) Программа должна распечатать через запятую все существительные женского рода единственного числа, а также вывести на экран сумму их ipm.
words = []
with open('words.txt','r', encoding = 'utf-8') as f:
    text = f.read()
    words = text.split('\n')

feminin = []
ipm = 0
word = ''
gram = ''
ipmi = ''
for i in range(len(words)):
    if 'сущ' in words[i] and  'жен' in words[i]:
        feminin.append(words[i])
        word, gram, ipmi = words[i].split('|') 
        ipm += float(ipmi)

for i in range(len(feminin)):
    print(feminin[i]+',')
print(ipm)
