list_list = [['l'],['s'],['d']]
def el_0(any_list):
    return any_list[0]

a = ' '.join([el_0(el) for el in list_list])
print(a)
## 'l s d'
b = list(map(el_0, list_list))
print(b)
## ['l', 's', 'd']
b = ' '.join(list(map(el_0, list_list)))
print(b)
## 'l s d'
c = ' '.join(list(map(lambda any_list: any_list[0], list_list)))
print(c)
## 'l s d'
