#Regulere Ausdrucke und Selbstformatierte
import re

#^ - gehört zum Anfang (Zeichen am Anfang)
#   ^spam - Zeile soll anfangen mit Zeichenkette spam

#$ - gehört zum Ende (Zeichen am Ende)
#   spam$ - Zeile soll enden mit zeichenkette spam

#+ - für ein oder mehr Zeichen
#\d - für Digitales/Nummerisches Zeichen
#\w - für Buchstaben
#\s - für Lehrzeichen/probel
#\D, \W, \S - ist das gegenteil von 3 oberen (also \D - für kein Digitales Zeichen u.s.w.)

#[abc] - jedes anzelne Sumbol a,b oder c
#[^abc] - jedes anzelne Sumbol AUSER a,b oder c
#. - ist für Gruppensumbol dabei ist .selbst ein belibiges Zeichen auser Zeichen \n
#.* - ist somit belibiges Text

#------------
#istStringNum = re.compile(r'^\d+$') #am Anfang und Ende soll ein oder mehr Ziffern vorkommen
#istStringNum.search('1234567890')
##match == '1234567890'
#print(istStringNum.search('12345qwert67890') == None)
##Ergebnis True
#print(istStringNum.search('12 34567890') == None)
##Ergebnis True
#print(istStringNum.search('dd 12 34567890 qwert') == None)
#------------

#------------
#atRegex = re.compile(r'.at')
#print(atRegex.findall('The cat in the hat sat on the flat mat. At und at'))
#------------

#------------
#nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
#mo = nameRegex.search('First Name: Allexander Last Name: Fortowski')
#print(mo.group(0)) #ist gleich - print(mo.group()) also alles
#print(mo.group(1))
#print(mo.group(2))
#------------

#------------Benutze mit ?-nicht geizige Suche (wie mit {})
nongreedyRegex=re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To server man> for one dinner.>')
print(mo.group())
mo1 = nongreedyRegex.search('<To server> man <for> one dinner.>')
print(mo1.group())

greedyRegex=re.compile(r'<.*>') #gaizige variante sucht nach der Lenste mögliche enlichkeit
mo = greedyRegex.search('<To server man> for wan dinner.>')
print(mo.group())
mo1 = greedyRegex.search('<To server> man <for> wan dinner.>')
print(mo1.group())
