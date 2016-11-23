##3 вариант
##abracadabra
##bracadabraa
##racadabraab
##acadabraabr
##cadabraabra
##adabraabrac
##dabraabraca
##abraabracad
##braabracada
##raabracadab
##aabracadabr

text = input('Type something: ')
for i in range(len(text)):
    print(text[i:]+text[:i])

