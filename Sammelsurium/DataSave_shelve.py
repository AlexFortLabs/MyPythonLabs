# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Um Daten aus Python-Programmen zu speichern nutze Modul  shelve
# --------------------------------------------------------
import shelve

# 1--------------------------------------------------------
#! Erstelen der Binare Datei
# --------------------------------------------------------
#shelveFile = shelve.open('BData')
#! wir bekommen 3 Binare-Dateien *.bak, *dat, *.dir
#cats = ['Zophie', 'Pooka', 'Mole', 'Jack']
#shelveFile['cats'] = cats
#shelveFile.close()

# 2--------------------------------------------------------
#! daten auslesen
# --------------------------------------------------------
#shelveFile = shelve.open('BData')
#print(type(shelveFile))
#print(shelveFile['cats'])
#! schlissen nicht vergessen
#shelveFile.close()

# 3--------------------------------------------------------
#! daten auslesen gezielt per metoden keys() & values()
# --------------------------------------------------------
shelveFile = shelve.open('BData')
print(list(shelveFile.keys()))
print(list(shelveFile.values()))

# schlissen nicht vergessen
shelveFile.close()
# --------------------------------------------------------