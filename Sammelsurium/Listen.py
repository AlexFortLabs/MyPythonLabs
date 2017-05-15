# Trik mit Gruppenzuweisung und...

cat=['fat', 'black', 'DE']
size, color, dispo = cat
print('Sitze ' + size)
print(color + '\n')
print(dispo)

Geburtstag = ['Hoh sol er leben!']
Geburtstag *=3
print(Geburtstag)

size += ' ist Cat'
print(size)

print(cat.index('black'))

cat.append('Milk')
print(cat)
cat.insert(3, 'chicken')
print(cat)

if color in cat:
    print('Kater ist ' + color)
else:
    print('farbe undefiniert')

if 'FR' not in cat:
    print('Bin ja kein Franzose')

cat.remove('DE')
#cat.del(1)
print(cat)

edv = ['Roh', 'Bar', 'For', 'Rem']
print(edv)
edv.sort()
print(edv)
edv.sort(reverse=True)
print(edv)

for n in range(len(edv)):
    print(edv[n])

spam = ['a', 'C', 'z', 'A', 'Z', 'k']
print(spam)
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)
