# Comma Separated Values.
# Но хотя формат csv - это формат текстовых файлов, Python для упрощения работы с ним предоставляет специальный встроенный модуль csv

import csv

FILENAME = "users.csv"

users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)

# При открытии файла на запись в качестве третьего параметра указывается значение newline="" - пустая строка
# позволяет корректно считывать строки из файла вне зависимости от операционной системы.

# Для чтения из файла нам наоборот нужно создать объект reader:
import csv

FILENAME = "users.csv"

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])

# Для записи нам надо получить объект writer, который возвращается функцией csv.writer(file). В эту функцию передается
# открытый файл. А запись производится с writer.writerows(users) Этот метод принимает набор строк. В нашем случае это двухмерный список.

# Если необходимо добавить одну запись, которая представляет собой одномерный список, например, ["Sam", 31], то
# в этом случае можно вызвать метод writer.writerow(user)

# Работа со словарями
# В примере выше каждая запись или строка представляла собой отдельный список, например, ["Sam", 31]. Но кроме того,
# модуль csv имеет специальные дополнительные возможности для работы со словарями. В частности, функция
#       csv.DictWriter() возвращает объект writer, который позволяет записывать в файл. А функция
#       csv.DictReader() возвращает объект reader для чтения из файла. Например:
import csv

FILENAME = "users.csv"

users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    # запись нескольких строк
    writer.writerows(users)

    user = {"name": "Sam", "age": 41}
    # запись одной строки
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])

# Запись строк также производится с помощью методов writerow() и writerows(). Но теперь каждая строка представляет собой
# отдельный словарь, и кроме того, производится запись и заголовков столбцов с помощью метода writeheader(),
# а в метод csv.DictWriter в качестве второго параметра передается набор столбцов.

# При чтении строк, используя названия столбцов, мы можем обратиться к отдельным значениям внутри строки: row["name"].