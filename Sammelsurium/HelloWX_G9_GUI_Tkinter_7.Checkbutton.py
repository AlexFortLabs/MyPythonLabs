# Checkbutton представляет собой флажок, который может находиться в двух состояниях: отмеченном и неотмеченном.

# Создадим простейший флажок:
from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

ismarried = IntVar()

ismarried_checkbutton = Checkbutton(text="Женат/Замужем", variable=ismarried)
ismarried_checkbutton.pack()

ismarried_label = Label(textvariable=ismarried)
ismarried_label.place(relx=.5, rely=.5, anchor="c")

root.mainloop()
# Отличительной чертой Checkbutton является возможность привязки к компоненту IntVar через параметр variable.
# В отмеченном состоянии привязанный компонент IntVar имеет значение 1, а в неотмеченном - 0. В итоге через IntVar мы
# можем получать значение, указанное пользователем.

# Конструктор Checkbutton принимает ряд параметров, с помощью которого можно настроить отображение флажков:
#       Checkbutton(master, options)
# Параметр master представляет ссылку на родительское окно, а параметр options представляет набор следующих параметров:
#       activebackground: фоновый цвет флажка в нажатом состоянии
#       activeforeground: цвет текста флажка в нажатом состоянии
#       bg: фоновый цвет флажка
#       bitmap: монохромное изображение для флажка
#       bd: граница вокруг флажка
#       command: ссылка на функцию, которая вызывается при нажатии на флажок
#       cursor: курсор при наведении на элемент
#       disabledforeground: цвет текста в состоянии DISABLED
#       font: шрифт
#       fg: цвет текста
#       height: высота элемента
#       image: графическое изображение, отображаемое на элементе
#       justify: выравнивание текста, принимает значения CENTER, LEFT, RIGHT
#       offvalue: значение ассоциированной с флажком переменной IntVar в неотмеченном состоянии, по умолчанию равно 0
#       onvalue: значение ассоциированной с флажком переменной IntVar в отмеченном состоянии, по умолчанию равно 1
#       padx: отступы справа и слева от текста до границы флажка
#       pady: отступы сверху и снизу от текста до границы флажка
#       relief: стиль флажка, по умолчанию имеет значение FLAT
#       selectcolor: цвет квадратика флажка
#       selectimage: изображение на флажке, когда он находится в отмеченном состоянии
#       state: состояние элемента, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE
#       text: текст элемента
#       underline: индекс подчеркнутого символа в тексте флажка
#       variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние флажка
#       width: ширина элемента
#       wraplength: устанавливает перенос символов на другую строку в тексте элемента

# Используем некоторые из этих параметров:
from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

python_lang = IntVar()
python_checkbutton = Checkbutton(text="Python", variable=python_lang, onvalue=1, offvalue=0, padx=15, pady=10)
python_checkbutton.grid(row=0, column=0, sticky=W)

javascript_lang = IntVar()
javascript_checkbutton = Checkbutton(text="JavaScript", variable=javascript_lang, onvalue=1, offvalue=0, padx=15, pady=10)
javascript_checkbutton.grid(row=1, column=0, sticky=W)

root.mainloop()
