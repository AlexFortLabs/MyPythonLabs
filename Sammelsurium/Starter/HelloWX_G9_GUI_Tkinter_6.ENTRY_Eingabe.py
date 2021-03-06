# Элемент Entry представляет поле для ввода текста. Конструктор Entry принимает следующие параметры:
#       Entry(master, options)
#       Где master - ссылка на родительское окно, а options - набор следующих параметров:
#       bg: фоновый цвет
#       bd: толщина границы
#       cursor: курсор указателя мыши при наведении на текстовое поле
#       fg: цвет текста
#       font: шрифт текста
#       justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю
#       relief: определяет тип границы, по умолчанию значение FLAT
#       selectbackground: фоновый цвет выделенного куска текста
#       selectforeground: цвет выделенного текста
#       show: задает маску для вводимых символов
#       state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED
#       textvariable: устанавливает привязку к элементу StringVar
#       width: ширина элемента

# Определим элемент Entry и по нажатию на кнопку выведем его текст в отдельное окно с сообщением:
from tkinter import *
from tkinter import messagebox


def show_message():
    messagebox.showinfo("GUI Python", message.get())


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="Click Me", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()

# Для вывода сообщения здесь применяется дополнительный модуль messagebox, содержащий функцию showinfo(), которая
# собственно и выводит введенный в текстовое поле текст. Для получения введенного текста используется комп StringVar,
# как было описано в одной из предыдущих тем.

# Теперь создадим более сложный пример с формой ввода:
from tkinter import *
from tkinter import messagebox


def display_full_name():
    messagebox.showinfo("GUI Python", name.get() + " " + surname.get())


root = Tk()
root.title("GUI на Python mu 2 Eingabefeldern")

name = StringVar()
surname = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

message_button = Button(text="Click Me", command=display_full_name)
message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()


# Методы Entry
# Элемент Entry имеет ряд методов. Основные из них:
#       insert(index, str): вставляет в текстовое поле строку по определенному индексу
#       get(): возвращает введенный в текстовое поле текст
#       delete(first, last=None): удаляет символ по индексу first. Если указан параметр last, то удаление производится
#                 до индекса last. Чтобы удалить до конца, в качестве второго параметра можно использовать значение END.

# sdИспользуем методы в программе:
from tkinter import *
from tkinter import messagebox

# Кнопка Clear очищает оба поля, вызывая метод delete
def clear():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)

# Вторая кнопка, используя метод get, получает введенный текст:
def display():
    messagebox.showinfo("GUI Python Entry Metoden", name_entry.get() + " " + surname_entry.get())
# как видно из примера, нам необязательно обращаться к тексту в Entry через переменные типа StringVar, мы можем
# это сделать напрямую через метод get.

root = Tk()
root.title("GUI на Python")

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry()
surname_entry = Entry()

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

# вставка начальных данных
name_entry.insert(0, "Tom")
surname_entry.insert(0, "Soyer")
# При запуске программы сразу же в оба текстовых поля добавляется текст по умолчанию:

display_button = Button(text="Display", command=display)
clear_button = Button(text="Clear", command=clear)

display_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()
