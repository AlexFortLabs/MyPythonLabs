# Метод pack
# Для позиционирования элементов в окне применяются различные способы, и самый простой способ представляет вызов
# у элемента метода pack(). Этот метод принимает следующие параметры:
#       expand: если равно True, то виджет заполняет все пространство контейнера.
#       fill: определяет, будет ли виджет растягиваться, чтобы заполнить свободное пространство вокруг. Этот параметр
#               может принимать следующие значения: NONE (по умолчанию, элемент не растягивается), X (элемент
#               растягивается только по горизонтали), Y (элемент растягивается только по вертикали) и BOTH (элемент
#               растягивается по вертикали и горизонтали).
#       side: выравнивает виджет по одной из сторон контейнера. Может принимать значения: TOP (по умолчанию,
#               выравнивается по верхней стороне контейнера), BOTTOM (выравнивание по нижней стороне), LEFT
#               (выравнивание по левой стороне), RIGHT (выравнивание по правой стороне).

# Например, растянем кнопку на всю форм, используя параметры expand и fill:
from tkinter import *

root = Tk()
root.title("GUI на Python 1")
root.geometry("300x250")

btn1 = Button(text="CLICK ME", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
btn1.pack(expand=True, fill=BOTH)

root.mainloop()


# Используем параметр side:
from tkinter import *

root = Tk()
root.title("GUI на Python 2")
root.geometry("300x250")

btn1 = Button(text="BOTTOM", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
btn1.pack(side=BOTTOM)

btn2 = Button(text="RIGHT", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
btn2.pack(side=RIGHT)

btn3 = Button(text="LEFT", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
btn3.pack(side=LEFT)

btn4 = Button(text="TOP", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
btn4.pack(side=TOP)

root.mainloop()

# Комбинируя параметры side и fill, можно растянуть элемент по вертикали:
#btn1 = Button(text="CLICK ME", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
#btn1.pack(side=LEFT, fill=Y)


# Метод place
# Метод place() позволяет более точно настроить параметры позиционирования. Он принимает следующие параметры:
#       height и width: устанавливают соответственно высоту и ширину элемента в пикселях
#       relheight и relwidth: также задают соответственно высоту и ширину элемента, но в качестве значения используется
#               число float в промежутке между 0.0 и 1.0, которое указывает на долю от высоты и ширины родительского контейнера
#       x и y: устанавливают смещение элемента по горизонтали и вертикали в пикселях соответственно относительно
#               верхнего левого угла контейнера
#       relx и rely: также задают смещение элемента по горизонтали и вертикали, но в качестве значения используется
#               число float в промежутке между 0.0 и 1.0, которое указывает на долю от высоты и ширины родительского контейнера
#       bordermode: задает формат границы элемента. Может принимать значение INSIDE (по умолчанию) и OUTSIDE
#       anchor: устанавливает опции растяжения элемента. Может принимать значения n, e, s, w, ne, nw, se, sw, c, которые
#               являются сокращениями от Noth(север - вверх), South (юг - низ), East (восток - правая сторона),
#               West (запад - левая сторона) и Center (по центру). Например, значение nw указывает на верхний левый угол

# Следует заметить, что при использовании метода place() не надо использовать метод pack(), чтобы сделать элемент видимым.

# Например, разместим кнопку с шириной 130 пикселей и высотой 30 пикселей в центре окна:
from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    btn.config(text="Clicks {}".format(clicks))


root = Tk()
root.title("GUI на Python 3")
root.geometry("300x250")

btn = Button(text="Clicks 0", background="#555", foreground="#ccc", padx="20", pady="8", font="16", command=click_button)
btn.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

root.mainloop()

# Следует заметить, что при использовании метода place() не надо использовать метод pack(), чтобы сделать элемент видимым.

# Или разместим три кнопки:
from tkinter import *

root = Tk()
root.title("GUI на Python 4")
root.geometry("300x250")

btn1 = Button(text="x=10, y=20", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
btn1.place(x=10, y=20)

btn2 = Button(text="x=50, y=100", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
btn2.place(x=50, y=100)

btn3 = Button(text="x=140, y=160", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
btn3.place(x=140, y=160)

root.mainloop()

# Метод grid
# Метод grid применяет другой подход к позиционированию элементов, нежели метод place, позволяя поместить элемент в
# определенную ячейку условной сетки или грида.

# Метод grid применяет следующие параметры:
#       column: номер столбца, отсчет начинается с нуля
#       row: номер строки, отсчет начинается с нуля
#       columnspan: сколько столбцов должен занимать элемент
#       rowspan: сколько строк должен занимать элемент
#       ipadx и ipady: отступы по горизонтали и вертикали соответственно от границ элемента до его текста
#       padx и pady: отступы по горизонтали и вертикали соответственно от границ ячейки грида до границ элемента
#       sticky: выравнивание элемента в ячейке, если ячейка больше элемента. Может принимать значения n, e, s, w, ne,
#               nw, se, sw, которые указывают соответствующее направление выравнивания

# Например, определим грид из 9 кнопок:
from tkinter import *

root = Tk()
root.title("GUI на Python 5")
root.geometry("300x250")

for r in range(3):
    for c in range(3):
        btn = Button(text="{}-{}".format(r, c))
        btn.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10)

root.mainloop()
