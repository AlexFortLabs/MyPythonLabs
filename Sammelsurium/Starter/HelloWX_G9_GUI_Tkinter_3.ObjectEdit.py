# изменить какие-то атрибуты кнопки, например, текст. Однако у той же кнопки нет никакого такого метода для изменения
# текста. И возникает вопрос, как же его можно изменить?
# Для изменения текста мы можем использовать промежуточный компонент StringVar. Этот компонент позволяет создать
# привязку к строке. Он имеет два методы:
#       get(): возвращает строку из StringVar
#       set(str): устанавливает строку в StringVar
# Для связи объекта StringVar с текстом визуального элемента у этого элемента в конструкторе надо установить
# параметр textvariable. Например, с помощью нажатия на кнопку пусть у нас изменяется ее текст:
from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    buttonText.set("Clicks {}".format(clicks))


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

buttonText = StringVar()
buttonText.set("Clicks {}".format(clicks))

btn = Button(textvariable=buttonText, background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()

root.mainloop()
# Здесь создается переменная buttonText, которая имеет тип StringVar. Для нее устанавливается начальное значение,
# а затем переменная btn связывается с этим текстом через параметр textvariable - при нажатии на кнопку изменится ее текст.

# Кроме компонента StringVar нам доступно еще ряд подобных компонентов для других типов данных:
#       IntVar
#       BooleanVar
#       DoubleVar

# Например, мы могли бы установить привязку к переменной IntVar и выводить количество кликов:
from tkinter import *


def click_button():
    clicks.set(clicks.get() + 1)


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

clicks = IntVar()
clicks.set(0)

btn = Button(textvariable=clicks, background="#555", foreground="#ccc",
             padx="20", pady="8", font="Verdana 13", command=click_button)
btn.pack()

root.mainloop()

# Метод config
# Но есть и другой способ, который особенно поможет, если нам надо изменять не только текст, но и другие параметры
# кнопки или другого компонента. Это способ заключается в вызове у элемента метода config(), в котором и устанавливается
# нужный параметр. Например, используем метод config, изменив код скрипта:
from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    btn.config(text="Clicks {}".format(clicks))


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn = Button(text="Clicks 0", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()

root.mainloop()
