Fa = "Krupski"
Na = "Silvia"
print(Fa + "\nVorname: " + Na)

def gibName(vornach, lang):
    #vorgang = ((vornach[:lang]).replace(' ', ''))
    vorgang = ((vornach.replace(' ', '')).replace('-', ''))
    ergebnis = ((vorgang.title())[:lang])
    return ergebnis

FaEr = gibName(Fa, 8)
# print (FaEr)
NaEr = gibName(Na, 2)
# print (NaEr)
ADName = FaEr + NaEr
print('AD Name: ' + ADName)
ADName_i5 = ADName.upper()
print ('i5 Name: ' + ADName_i5)
