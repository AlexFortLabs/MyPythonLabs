# Radiobutton представляет переключатель, который может находиться в двух состояниях: отмеченном или неотмеченном.
# Но в отличие от Checkbutton переключатели могут создавать группу, из которой одномоментно мы можем выбрать только один переключатель.

# Используем переключатели:
from tkinter import *

root = Tk()
root.title("GUI на Python mit Radiobuttons")
root.geometry("300x250")

header = Label(text="Выберите курс", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

lang = IntVar()

python_checkbutton = Radiobutton(text="Python", value=1, variable=lang, padx=15, pady=10)
python_checkbutton.grid(row=1, column=0, sticky=W)

javascript_checkbutton = Radiobutton(text="JavaScript", value=2, variable=lang, padx=15, pady=10)
javascript_checkbutton.grid(row=2, column=0, sticky=W)

selection = Label(textvariable=lang, padx=15, pady=10)
selection.grid(row=3, column=0, sticky=S)

root.mainloop()
# Здесь определены два переключателя, но оба они привязаны к одной переменной IntVar. При этом они имеют разные значения,
# устанавливаемые через параметр value. Поэтому при включении одного переключателя, другой автоматически перейдет в неотмеченное состояние.

# Для настройки переключателя конструктор Radiobutton, как и другие конструкторы виджетов, принимает два параметра:
#       Radiobutton (master, options)
# Первый параметр - master представляет ссылку на родительское окно, а второй параметр объединяет набор следующих параметров:
#       activebackground: фоновый цвет переключателя в нажатом состоянии
#       activeforeground: цвет текста переключателя в нажатом состоянии
#       bg: фоновый цвет переключателя
#       bitmap: монохромное изображение для переключателя
#       borderwidth: граница вокруг переключателя
#       command: ссылка на функцию, которая вызывается при нажатии на переключатель
#       cursor: курсор при наведении на элемент
#       font: шрифт
#       fg: цвет текста
#       height: высота элемента в строках текста. По умолчанию равно 1
#       image: графическое изображение, отображаемое на элементе
#       justify: выравнивание текста, принимает значения CENTER, LEFT, RIGHT
#       padx: отступы справа и слева от текста до границы переключателя
#       pady: отступы сверху и снизу от текста до границы переключателя
#       relief: стиль переключателя, по умолчанию имеет значение FLAT
#       selectcolor: цвет кружка переключателя
#       selectimage: изображение на переключателе, когда он находится в отмеченном состоянии
#       state: состояние элемента, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE
#       text: текст элемента
#       textvariable: устанавливает привязку к переменной StringVar, которая задает текст переключателя
#       underline: индекс подчеркнутого символа в тексте элемента
#       variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние переключателя
#       value: значение переключателя
#       width: ширина элемента
#       wraplength: устанавливает перенос символов на другую строку в тексте элемента

# Используем ряд этих параметров в более сложном примере с обработкой выбора пользователя:
from tkinter import *

languages = [("Python", 1), ("JavaScript", 2), ("C#", 3), ("Java", 4)]


def select():
    l = language.get()
    if l == 1:
        sel.config(text="Выбран Python")
    elif l == 2:
        sel.config(text="Выбран JavaScript")
    elif l == 3:
        sel.config(text="Выбран C#")
    elif l == 4:
        sel.config(text="Выбран Java")


root = Tk()
root.title("GUI на Python")
root.geometry("300x280")

header = Label(text="Выберите курс", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

language = IntVar()

row = 1
for txt, val in languages:
    Radiobutton(text=txt, value=val, variable=language, padx=15, pady=10, command=select).grid(row=row, sticky=W)
    row += 1

sel = Label(padx=15, pady=10)
sel.grid(row=row, sticky=W)

root.mainloop()
