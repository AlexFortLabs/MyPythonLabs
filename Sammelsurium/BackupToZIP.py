# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Python 3 - Kopiere Gesamtinhalt des Folder in ZIP-File
# und vergebe weiteres freies Nummer für den Archiv
# --------------------------------------------------------
import zipfile, os

def backupToZip(folder):
    # Erstelle ZIP-File aus dem Gesamtinhalt des "folder"

    folder = os.path.abspath(folder) # prüfe ob das die absolute Path ist?
    # Automatische Nummerierung für den Archiv(n) auf Grund von vorhandenen Archiven
    nextNumber = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(nextNumber) + '.zip'
        if not os.path.exists(zipFilename):
            break
        nextNumber += 1
    # Erstelle ZIP-File
    print('Erstelle Archiv %s.' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Im Durchgang durch den Ordner und deren Unterordner werden alle Files komprimiert
    for foldername, subfolders, filenames in os.walk(folder):
        print('Zufügen von Dateien aus dem Ordner %s' % (foldername))
        # Aktuelle Ordner zum Archiv hinzufügen
        backupZip.write(foldername)
        # alle Dateien aus diesem Ordner hinzufügen
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if (filename.startswith(newBase) or filename.endswith('.zip')): # ZIP-Files werden nicht mitgesichert
                #print(newBase) #continue                # install_ z.B fuer C:\install\temp\DatafactoryCargo_q3-2016.zip
                #print(filename.startswith(newBase))     # False
                #print(filename.endswith('.zip'))        # True
                print('Nicht mitgesichert %s.' % os.path.join(foldername, filename))
            else:
                backupZip.write(os.path.join(foldername, filename))

    backupZip.close()

    print('Erledigt')

# Welcher Ordner soll gesichert werden
backupToZip('C:\\install')

