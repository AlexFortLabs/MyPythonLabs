# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# In einem Verzeichnis werden alle Unterordner
# (aber nur eine Ebene tiefer), nach Dateien
# mit bestimmten Endungen gesucht um diese dann zu verarbeiten.
# --------------------------------------------------------
import os

source_dir = '\\\\funkegruppe.de\\userdata\\Userlaufwerk'
#file_basename = 'desktop'

for myDirEbene2 in os.listdir(source_dir):
    for filename in os.listdir(os.path.join(source_dir, myDirEbene2)):
        #if filename.endswith('.txt') or filename.endswith('.html'):
        #if filename.endswith('.ini') and os.path.basename(filename) == 'desktop' : # !FEHLER!
        if filename == 'desktop.ini':
            # mach was - lösche die gefundene Datei
            #os.unlink(os.path.join(source_dir, myDirEbene2, filename))
            # und zeige was gelöscht ist
            print(os.path.join(source_dir, myDirEbene2, filename))
