## 2. Пользователь вводит число, например, 3. Нужно создать количество папок в соответствии с введенным числом.
## В нашем случае это три папки, которые должны называться "1", "2", "3". В первой папке нужно создать один текстовый файл,
## во второй два файла, в третьей - три файла и т.д.

import shutil
import os

num = int(input('Print any natural number. '))

for i in range(num):
    name = str(i+1)
    os.makedirs(name)
    for a in range(i+1):
        filename = os.path.join(name,str(a+1)+'.txt')
        with open(filename, 'w', encoding = 'utf-8') as f:
            f.write('')
