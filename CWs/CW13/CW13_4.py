## 4. Распечатать, сколько в заданной папке (например, в текущей) файлов с различными расширениями, например:
## txt        3
## csv        1
## xls        8

import os
import shutil

directory = input('Print any path working in your OS. ')
if os.path.exists(directory):
    filelist = [f for f in os.listdir() if os.path.isfile(f)]
    extlist = []
    for f in filelist:
        ext = f.split('.')[1]
        if ext not in extlist:
            extlist.append(ext)
    extdict = {}
    for ext in extlist:
        for f in filelist:
            if f.endswith(ext):
                if ext not in extdict:
                    extdict[ext] = 1
                else:
                    extdict[ext] +=1
else:
    directory = os.getcwd()

print(extdict)

