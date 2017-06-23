# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Dateien und Ordner kopieren
# --------------------------------------------------------
import shutil, os

os.chdir('C:\\')

#! Dateien kopieren
#shutil.copy('C:\\install\\quarantene\\Virenfunde.html', 'C:\\install')
#shutil.copy('test.txt', 'C:\\install\\temp\ordner1\\test2.txt')

#! Ordner kopieren
#shutil.copytree('C:\\install\\temp', 'C:\\install\\temp2')

#! Dateien verschieben/ersetzen
#shutil.move('C:\\install\\temp\ordner1\\test2.txt', 'C:\\install')                      # Name bleibt
shutil.move('C:\\install\\temp\ordner1\\test2.txt', 'C:\\install\\test002.txt')         # Name geaendert
