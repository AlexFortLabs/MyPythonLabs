# Listbox в tkinter представляет список объектов. Определим простой список:
from tkinter import *

languages = ["Python", "JavaScript", "C#", "Java"]

root = Tk()
root.title("GUI на Python")
root.geometry("300x280")

languages_listbox = Listbox()

for language in languages:
    languages_listbox.insert(END, language)

languages_listbox.pack()

root.mainloop()
# Для наполнения listboxa элементами в цикле for пробегаемся по всем элементам списка languages и добавляем каждый
# элемент в listbox с помощью метода insert(). В качестве первого аргумента в insert передается индекс вставки элемента.
# Но если мы хотим последовательно добавить элементы, то вместо индекса можно использовать значение END.

# Для настройки виджета Listbox мы можем указать в его конструкторе следующие параметры:
#       bg: фоновый цвет
#       bd: толщина границы вокруг элемента
#       cursor: курсор при наведении на Listbox
#       font: настройки шрифта
#       fg: цвет текста
#       height: высота элемента в строках. По умолчанию отображает 10 строк
#       highlightcolor: цвет элемента, когда он получает фокус
#       highlightthickness: толщина границы элемента, когда он находится в фокусе
#       relief: устанавливает стиль элемента, по умолчанию имеет значение SUNKEN
#       selectbackground: фоновый цвет для выделенного элемента
#       selectmode: определяет, сколько элементов могут быть выделены. Может принимать следующие значения: BROWSE,
#                   SINGLE, MULTIPLE, EXTENDED. Например, если необходимо включить множественное выделение элементов,
#                   то можно использовать значения MULTIPLE или EXTENDED.
#       width: устанавливает ширину элемента в символах. По умолчанию ширина - 20 символов
#       xscrollcommand: задает горизонтальную прокрутку
#       yscrollcommand: устанавливает вертикальную прокрутку

# Некоторую сложность при использовании Listbox представляет создание прокрутки. Рассмотрим, как это сделать:
from tkinter import *

languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
             "T-SQL", "PL-SQL", "Typescript"]

root = Tk()
root.title("GUI на Python")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

languages_listbox = Listbox(yscrollcommand=scrollbar.set, width=40)

for language in languages:
    languages_listbox.insert(END, language)

languages_listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=languages_listbox.yview)

root.mainloop()
# Для создания прокрутки создается элемент Scrollbar. И так как необходимо прокручивать listbox по вертикали, то у него
# задается параметр yscrollcommand=scrollbar.set
# В конце scrollbar ассоциируется с функцией, которую надо выполнять при прокрутке. В данном случае это метод yview
# элемента listbox. В итоге мы сможем прокручивать элементы по вертикали.

# Основные методы Listbox
# Listbox имеет ряд методов для управления поведением элемента и его содержимым. Некоторые из них:
#       curselection(): возвращает набор индексов выделенных элементов
#       delete(first, last = None): удаляет элементы с индексами из диапазона [first, last]. Если второй параметр опущен,
#               то удаляет только один элемент по индексу first.
#       get(first, last = None): возвращает кортеж, который содержит текст элементов с индексами из дипазона [first, last].
#               Если второй параметр опущен, возвращается только текст элемента с индексом first.
#       insert(index, element): вставляет элемент по определенному индексу
#       size(): возвращает количество элементов

# Для рассмотрения этих методов напишем небольшой скрипт по управлению данными:
from tkinter import *

# Вторая кнопка по нажатию удаляет выделенный элемент. Для этого мы сначала получаем выделенные индексы через
# метод curselection(). Так как в нашем случае выделяется только один элемент, то получаем его индекс через
# выражение selection[0]. И этот индекс передаем в метод delete() для удаления
def delete():
    selection = languages_listbox.curselection()
    # мы можем получить удаляемый элемент по индексу
    # selected_language = languages_listbox.get(selection[0])
    languages_listbox.delete(selection[0])


# добавление нового элемента
def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)


root = Tk()
root.title("GUI на Python")

# текстовое поле и кнопка для добавления в список
language_entry = Entry(width=40)
language_entry.grid(column=0, row=0, padx=6, pady=6)
add_button = Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
# кнопка вызывает функцию add(), которая получает введенное в текстовое поле значение и добавляет его на первое место в списке с помощью метода insert().

# создаем список
languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=W + E, padx=5, pady=5)

# добавляем в список начальные элементы
languages_listbox.insert(END, "Python")
languages_listbox.insert(END, "C#")

delete_button = Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
