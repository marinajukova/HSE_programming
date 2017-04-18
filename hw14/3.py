## 3. Программа должна обходить всё дерево папок, начинающееся с той папки, где она находится, и сообщать
## файлы с каким расширением чаще всего встречаются в этих папках (если таких много, можно печатать только одно)

import os


extension_frequency_list = {}

for root, dirs, files in os.walk('.'):
    for f in files:
        file_name = f.split('.')[0]
        file_ext = f.split('.')[1]
        if file_ext not in extension_frequency_list:
            extension_frequency_list[file_ext] =  1
        else:
            extension_frequency_list[file_ext] +=  1

max_ext = max(extension_frequency_list.values())
i = 0
for key in extension_frequency_list:
    if extension_frequency_list[key] == max_ext:
        if i == 0: 
            print('The most frequent extention is \''+key+'\'. There is(are) '+str(extension_frequency_list[key])+' file(s) with it.')
            i = 1
        else:
            print('There is(are) also '+str(extension_frequency_list[key])+' \''+key+'\' file(s).')
