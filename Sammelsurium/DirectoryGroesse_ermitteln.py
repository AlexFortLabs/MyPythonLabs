# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Hello Python 3
# --------------------------------------------------------
import os

testPath = 'C:\\Windows\\System32\\calc.exe'
testPath2 = 'C:\\Windows\\System32'
# Dateigroesse in Byte
print(os.path.getsize(testPath))

# Ordner Inhalt auflisten'
#print(os.listdir(testPath2))

# Gesamtgroesse des Ordnerinhalt ermitteln
totalSitze = 0
for filename in os.listdir(testPath2):
    totalSitze = totalSitze + os.path.getsize(os.path.join(testPath2, filename))

print(totalSitze)
