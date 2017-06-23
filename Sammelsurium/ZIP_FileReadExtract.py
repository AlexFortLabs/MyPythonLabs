# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Objekt mitels Funktion zipfile.ZipFile() erstellen und:
# --------------------------------------------------------
import zipfile, os

os.chdir('C:\\install\\temp')   # gehe zum Ordner mit Zip-Archiv
myZipFile = zipfile.ZipFile('DatafactoryCargo_q3-2016.zip')     # erstelle Objekt ZipFile

# --------------------------------------------------------
#! Inhalte des ZIP-Archivs zeigen mit Zusatz Info zu Komprimierung
myZipFileInhalt = (myZipFile.namelist())            # Metdode namelist() gibt zurück eine Liste mit Inhalt
print(myZipFileInhalt)

for archivFile in myZipFileInhalt:
    spamInfo = myZipFile.getinfo(archivFile)
    print(archivFile, ' Size: ', spamInfo.file_size, ' Komprimiert auf: ', spamInfo.compress_size)

# --------------------------------------------------------
#! Einzeln aus ZIP-Archiv endpacken
#myZipFile.extract('FD.DAT')     # eine Datei aus dem Archiv in aktuelles Ordner
#myZipFile.extract('FD.DAT', 'C.\\mein\\new\\folder')  # eine Datei aus dem Archiv in bestimtes Ordner

#! endpackt ALLES und überschreibt vorhandenes
#! myZipFile.extractall() - endpackt ALLES in gleiches Ordner
myZipFile.extractall('C:\\install\\Cargo')      # ALLES endpacken gezilt in Ordner - dieser wird erstehlt wenn nicht vorhanden

# Object/File schlissen
myZipFile.close()