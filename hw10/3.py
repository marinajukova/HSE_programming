## 3. Программа должна открывать заранее сохранённый html-файл со статьёй из русской википедии о вузе с карточкой
## и доставать оттуда количество преподавателей. Извлеченную информацию она должна записать в текстовый файл.


import re

def main():
    with open ('hse.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    card_reg = '<table class="infobox vcard"(?:.|\n)+?</table>'
    if re.search(card_reg, text):
        card = re.search(card_reg, text).group()
        t_reg = 'Преподаватели(?:.|\n)*?<p>(.+?)<'
        if re.search(t_reg, card):
            profs = re.search(t_reg, card).group(1)
            with open ('data about teachers.txt', 'a', encoding = 'utf-8') as f:
                f.write(profs)
        else:
            print('No data about the nuber of professors found!')
            with open ('data about teachers.txt', 'a', encoding = 'utf-8') as f:
                f.write('No data about the nuber of professors found!')
    else:
        print('No card found in this article!')
        with open ('data about teachers.txt', 'a', encoding = 'utf-8') as f:
                f.write('No card found in this article!')
    
if __name__ == '__main__':
    main()
