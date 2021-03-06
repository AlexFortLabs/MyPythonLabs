# Меню может содержать много элементов, причем эти элементы сами могут представлять меню и содержать другие элементы.
# В зависимости от того, какой тип элементов мы хотим добавить в меню, будет отличаться метод, используемый для их
# добавления. В частности, нам доступны следующие методы:
#       add_command(options): добавляет элемент меню через параметр options
#       add_cascade(options): добавляет элемент меню, который в свою очередь может представлять подменю
#       add_separator(): добавляет линию-разграничитель
#       add_radiobutton(options): добавляет в меню переключатель
#       add_checkbutton(options): добавляет в меню флажок

# Создадим простейшее меню:
from tkinter import *

root = Tk()
root.title("GUI на Python Menu")
root.geometry("300x250")

main_menu = Menu()
main_menu.add_cascade(label="File")
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")

root.config(menu=main_menu)
root.mainloop()
# Для добавления пунктов меню у объекта Menu вызывается метод add_cascade(). В этот метод передаются параметры пункта
# меню, в данном случае они представлены текстовой меткой, устанавливаемой через параметр label. Но просто создать
# меню - еще недостаточно. Его надо установить для текущего окна с помощью параметра menu в методе config()

# Теперь добавим подменю:
from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")
# определяется подменю file_menu, которое добавляется в первый пункт основного меню благодаря установке опции menu=file_menu:

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")

root.config(menu=main_menu)

root.mainloop()

# Если необходимо настроить меню, то мы можем задать в конструкторе Menu следующие опции:
#       activebackground: цвет активного пункта меню
#       activeborderwidth: толщина границы активного пункта меню
#       activeforeground: цвет текста активного пункта меню
#       bg: фоновый цвет
#       bd: толщина границы
#       cursor: курсор указателя мыши при наведении на меню
#       disabledforeground: цвет, когда меню находится в состоянии DISABLED
#       font: шрифт текста
#       fg: цвет текста
#       tearoff: меню может быть отсоединено от графического окна. В частности, при создании подменю а скриншоте можно
#               увидеть прерывающуюся линию в верху подменю, за которую его можно отсоединить. Однако при значении
#               tearoff=0 подменю не сможет быть отсоединено.
from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

main_menu = Menu()

file_menu = Menu(font=("Verdana", 13, "bold"), tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")

root.config(menu=main_menu)

root.mainloop()


# Взаимодействие с меню
# у каждого элемента меню можно задать параметр command, который устанавливает ссылку на функцию, выполняемую при нажатии
from tkinter import *
from tkinter import messagebox


def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

main_menu = Menu()

main_menu.add_cascade(label="File")
main_menu.add_cascade(label="Edit", command=edit_click)
main_menu.add_cascade(label="View")

root.config(menu=main_menu)

root.mainloop()
