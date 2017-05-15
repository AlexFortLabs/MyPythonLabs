allGuests = {'Edgar' : {'apples':5, 'pretzels':12},
             'Jan' : {'sandwiches':3, 'apples':2, 'cakes' : 5, 'cups' : 2},
             'Julia' : {'cups' : 3, 'apple pies':2}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v  in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Was wurde mitgebracht')

print(' - Apples   ' + str(totalBrought(allGuests, 'apples')))    

print(' - Cups     ' + str(totalBrought(allGuests, 'cups')))    

print(' - Cakes     ' + str(totalBrought(allGuests, 'cakes')))

print(' - Sandwiches     ' + str(totalBrought(allGuests, 'sandwiches')))

print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies'))) 
