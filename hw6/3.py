##3.
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

table = []
text = input('Type something: ')
for i in range(len(text)):
    table.append(text[i:]+text[:i])
print(*table)

