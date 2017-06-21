# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Hello Python 3
# --------------------------------------------------------
import os

myPhad = "C:\\install\\temp\\ordner"

# --------------------------------------------------------
# Erstehlt Ordner von 0 bis C:\install\temp\ordner9
# aber nur wenn diese nicht vorhanden sind
#for myOrdnerNr in range(10):
#    os.makedirs(myPhad + str(myOrdnerNr))
    #print(myPhad + str(myOrdnerNr))
# --------------------------------------------------------
print(os.path.abspath('.'))
# ergebnis C:\GitHub\MyPythonLabs\Sammelsurium

print(os.path.abspath('.\\temp2\\temp'))
# ergebnis C:\GitHub\MyPythonLabs\Sammelsurium\temp2\temp

# ermittelten ob absoluten Pfad oder relativen Pfad vorliegt
print(os.path.isabs('.'))                       # False - weil Argument ist Relatives path
print(os.path.isabs(os.path.abspath('.')))      # True - weil Argument ist Absolutes path

# --------------------------------------------------------
# base-Name vom Pfad ermitteln (ist immer hinter letzetm \-Zeichen
testPath = 'C:\\Windows\\System32\\calc.exe'
myBaseName = os.path.basename(testPath)
print('My basename: ' + myBaseName)

myDirName = os.path.dirname(testPath)
print('My directory: ' + myDirName)

# wenn wir beides, Basename und Directory benötigen dann
# nutze split um Kortege erstellen mit dem Inhalt von beiden Teilen:
myKorteg = (os.path.split(testPath))
print(myKorteg)
print(myKorteg[1])