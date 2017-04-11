## 3. Программа должна просмотреть все папки и файлы, находящиеся в одной папке с ней, и сообщить 
## cколько найдено папок, название которых состоит только из кириллических символов.
## Кроме этого, программа должна выводить на экран названия всех файлов или папок, которые она нашла, без повторов.

import re
import os
import shutil

flist = os.listdir(os.getcwd())
clist =  []
cfcount = 0
for n in flist:
    cyrillic = 1
    name = n.split('.')[0]
    for let in name:
        if not re.match('[А-Яа-яЁё]',let):
            cyrillic = 0
    if cyrillic == 1:
        if os.path.isdir(n):
            cfcount += 1
        if name not in clist:
            clist.append(name)

print(cfcount)
print(clist)

