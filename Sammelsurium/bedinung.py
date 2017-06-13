import math

a = 3
if a in range(10):
    print("OK")

# Pruefe ob die a in Menge vorhanden ist?    
menge = [2, 5, 10, 3]
if a in menge:
    print(a, " ist in ", menge)


n = int(input('Введите целое число '))
#if chet(n):
if (n % 2 == 0):    
    print('Это число четное')
else:
    print('Это число нечетное')

# Zeige nur negative Werte
menge = [3, 5, 8, -4, 6, -93, 23]

for zahl in menge:
    if zahl < 0 :
        print(zahl)

# Zeige vertikales Lineal
for z in range(10, 30):
    if z % 10 == 5:
        print(z)
    else:
        print(".")
