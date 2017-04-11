## 3. Распечатать названия всех объектов в текущей папке, которые являются папками, а не файлами.

import os
import shutil

filelist = [f for f in os.listdir() if os.path.isfile(f)]
print(filelist)
