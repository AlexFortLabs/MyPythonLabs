# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# os.unlink - delete file im gezeigtem Pfad
# os.rmdir -  delete tree diese sollen lehr sein
# os.rmtree - delete tree zusammen mit deren Inhalt
# --------------------------------------------------------
import os

for filename in os.listdir('C:\ListenTXT'):
    if filename.endswith('.txt') or filename.endswith('.html'):
        #os.unlink(filename)      # lösche die gefundene Datei
        print(filename)           # zeige was gelöscht ist

