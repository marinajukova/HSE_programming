## Пользователь вводит предложение на английском языке, и программа создает вложенные друг в друга папки,
## так чтобы путь к самой глубокой из них составлял введенное предложение.
## Например, если пользователь ввел предложение "It is a wonderful day", программа должна создать вложенные папки,
## и путь к последней из них должен быть "it/is/a/wonderful/day"

import shutil
import os

name = input('Print any sentence. ')
words = name.split()
path = words[0]
for i in range(1, len(words)):
    path = os.path.join(path, words[i])
os.makedirs(path)
