## В этом коде есть баги.
import os ## В Windows путь указывается через \, а в Mac и Linux через /, кодировка по умолчанию у Windows cp1251 - это беда, надо указывать utf-8
import shutil


path = os.path.abspath('.') ## Путь к текущей папке
path2 = os.getcwd() ## Путь к текущей папке
universalpath = os.path.join('texts', '1.txt')
exists = os.path.exists('texts\1.txt') ## Проверяет существование пути
exists2 = os.path.exists(os.path.join('texts', '1.txt'))
filelist = os.listdir(r'C:\My\HSE\programming\HSE_programming\HSE_programming\CWs\CW13\texts') ## Что лежит в папке texts

s = 'Hello! '
i = 1
for f in filelist:
    if f.endswith('.txt'):
        with open(f, 'a', encoding = 'utf-8') as w:
            w.write(s*1)
            i += 1
texts = [f for f in os.listdir(r'C:\My\HSE\programming\HSE_programming\HSE_programming\CWs\CW13\texts') if f.endswith('.txt')]

if not os.path.exists('ab'):
    os.mkdir('ab') ## Создать путь
if not os.path.exists(r'a\long\long\long\long\path'):
    os.makedirs(r'a\long\long\long\long\path') ## Создать путь
if os.path.exists('ab') and not os.path.exists('abc'):
    os.rename('ab', 'abc')
if os.path.exists(r'a\long\long\long') and not os.path.exists(r'a\long\long\longer'):
    os.rename(r'a\long\long\long', r'a\long\long\longer')
isfile = os.path.isfile(r'texts\1.txt') ## Является ли файлом 
isdir = os.path.isdir(r'a\long\long') ## Является ли папкой

print(os.listdir())
shutil.copy(r'texts\1.txt', r'newcorpus') ## Копировать файл
shutil.copytree(r'texts', r'corpus') ## Копировать папку
shutil.move(r'texts\2.txt', r'newcorpus') ## Переместить файл

os.remove(r'corpus\2.txt') ## Удалить файл
shutil.rmtree('newcorpus') ## Удалить папку
shutil.rmtree('a')
shutil.rmtree('abc') 
