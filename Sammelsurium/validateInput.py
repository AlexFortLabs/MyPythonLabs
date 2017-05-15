while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Bitte Zahlen eingeben, desimal.')
    
while True:
    print('Gib Password ein: ')
    password=input()
    if password.isalnum():
        break
    print('Password soll nur Buchstabben und/oder Zeilen erhalten.')
    
