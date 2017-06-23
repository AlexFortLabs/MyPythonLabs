# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Um Daten aus Python-Programmen zu speichern als eigenes Modul im py-Format
# Meine Variablen werden gesichert mit Funktion pprint.format()
# in eine einfache Textdatei, die normal editierbar ist
# --------------------------------------------------------
import pprint

# --------------------------------------------------------
# Unser DatemPyModul erstellen
# --------------------------------------------------------
#cats = [{'name': 'Mole', 'desc': 'chubby', 'Nr': '96'}, {'name': 'Jack', 'desc': 'fluffy', 'Nr': '96A'}]
#pprint.pformat(cats)

#fileObj = open('myCats.py', 'w')
#fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
#fileObj.close()

# --------------------------------------------------------
# Unser DatenPyModul einlesen
# --------------------------------------------------------
import myCats
print(myCats.cats)

print(myCats.cats[1])

print(myCats.cats[1]['Nr'])

# --------------------------------------------------------