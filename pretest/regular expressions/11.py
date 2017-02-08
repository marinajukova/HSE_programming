##Скачайте любую статью из Википедии.
## извлеките из неё все HTML-тэги
## извлеките из неё только текст, очищенный от HTML-тэгов


import re

def clean(html):
    noscript = re.sub('<script[^<>]*?>[^<>]*?</script>', '', html)
    nostyle = re.sub('<style[^<>]*?>[^<>]*?</style>', '', noscript)
    nospan = re.sub('<span[^<>]*?>[^<>]*?</span>', '', nostyle)
    notags = re.sub('<[^>]*>', '', nospan)
    notags1 = re.sub('{[^}]*}', '', notags)
    text = re.sub('[&][^;]*;', ' ', notags1)
    text = re.sub(r'\s+', ' ', text)
    return text

def html(text):
    tags = re.findall(r'<[^>]*?>', text)
    return tags

def main():
    with open('schizo.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
        with open('html.txt', 'w', encoding = 'utf-8') as f:
            output = f.write('\n'.join(html(text)))
    with open('pure.txt', 'w', encoding = 'utf-8') as f:
        output = f.write(clean(text))

if __name__ == '__main__':
    main()
