# Arbeiten mit aktuelen Pfad in Python
import os
# Zeige aktueles Direktory - cwd
print(os.getcwd())

myFile = ['account.txt', 'details.csv', 'invite.doc']

print(" \/" * 20)
# aendere aktueles Direktory auf
os.chdir('C:\\Windows\\System32')   # unter Windows
#os.chdir('/home/cg')               # unter Linux

# unsiversal nach OS Ordner zum relativem Pfad verbinden
for filename in myFile:
    print(os.path.join(os.getcwd(), 'usr', 'bin', 'spam', filename))

print(" /\\" * 20)