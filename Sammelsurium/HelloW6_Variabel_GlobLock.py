name = "Tom"

def say_hi():
    print("Hello", name)

def say_bye():
    name = "Bob"
    print("Good bye", name)

say_hi()    # Hello Tom
say_bye()   # Good bye Bob

# Если же мы хотим изменить в локальной функции глобальную переменную, а не определить локальную,
# то необходимо использовать ключевое слово global:
def say_byebye():
    global name
    name = "Bobyk"  # Globale Variabel wird geaendert auf Bobyk
    print("Good bye", name)

say_byebye()    # Good bye Bobyk
say_hi()        # Hello Bobyk

PI = 3.14   # Bitte verwende Glob.Variablen nur für Konstanten - die unverändert bleiben wehrend des Programmlaufs
# вычисление площади круга
def get_circle_square(radius):
    print("Площадь круга с радиусом", radius, "равна", PI * radius * radius)

get_circle_square(50)