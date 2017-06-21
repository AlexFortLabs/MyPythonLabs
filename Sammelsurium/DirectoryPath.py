# Arbeiten mit aktuelem Pfad in Python
import os
# Zeige den aktuelen Pfad/Direktory in dem wir uns befinden - get cwd
print(os.getcwd())

myFile = ['account.txt', 'details.csv', 'invite.doc']

print(" \/" * 20)

# aendere die aktuele Position/Direktory auf - ch dir
os.chdir('C:\\Windows\\System32')   # unter Windows
#os.chdir('/home/cg')               # unter Linux

# universale Methode ja nach OS Win/Linux, die Dateien oder Ordner zum relativem Pfad verbinden.
# Hier werden Files aus der Liste myFiles mit dem Ordnerpfad zusammengesetzt.
# os.path.join() - erstellt korrekte Paths für unterschiedliche OSysteme
for filename in myFile:
    print(os.path.join(os.getcwd(), 'usr', 'bin', 'spam', filename))

# ERGEBNIS unter Windows ist:
# C:\Windows\System32\usr\bin\spam\account.txt
# ERGEBNIS unter Linux ist:
# /home/cg/usr/bin/spam/account.txt
print(" /\\" * 20)
