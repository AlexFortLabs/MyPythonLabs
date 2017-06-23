# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Spazieren durch die Verzeichnisse
# --------------------------------------------------------
import os

for folderName, subfolders, fileNames in os.walk('C:\\install'):
    print('Inhalt vom Ordner - ' + folderName)

    for subfolder in subfolders:
        print('Unterordner im Ordner ' + folderName + ': ' + subfolder)

    for fileName in fileNames:
        print('File im Ordner ' + folderName + ': ' + fileName)

    print(' ')