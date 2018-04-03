# tkinter доступен в виде отдельного встроенного модуля, который содержит все необходимые графические компоненты - кнопки, текстовые поля и т.д.
# Базовым моментом в построении графических программ является создание окна. Затем в окно добавляются все остальные
# компоненты графического интерфейса. Поэтому создадим вначале простейшее окно. Для этого определим следующий скрипт:
from tkinter import *

root = Tk()
root.title("Графическая программа на Python")
# root.geometry("400x300")
root.geometry("400x300+300+250")        # формат: "Ширина x Высота + координатаX + координатаY". То есть при запуске
# окно будет находиться на 300 пикселей вправо и на 250 пикселей вниз от верхнего левого угла экрана

root.mainloop()
# Для создания графического окна применяется конструктор Tk(), который определен в модуле tkinter. Создаваемое окно
# присваивается переменной root, и через эту переменную мы можем управлять атрибутами окна. В частности,
# с помощью метода title() можно установить заголовок окна.

# С помощью метода geometry() - размер окна. Для установки размера в метод geometry() передается строка в
# формате "Ширина x Высота". Если при создании окна приложения метод geometry() не вызывается, то окно занимает
# то пространство, которое необходимо для размещения внутреннего содержимого. По умолчанию окно позиционируется
# в верхний левый угол экрана. Но мы можем изменить его положение, передав нужные значения в метод geometry()

# Для отображения окна надо вызвать у него метод mainloop(), который запускает цикл обработки событий окна для взаимодействия с пользователем.