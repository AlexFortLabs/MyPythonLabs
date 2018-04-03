# Запись в текстовый файл
# Чтобы открыть текстовый файл на запись, необходимо применить режим w (перезапись) или a (дозапись). Затем для записи
# применяется метод write(str), в который передается записываемая строка. Стоит отметить, что записывается именно с
# трока, поэтому, если нужно записать числа, данные других типов, то их предварительно нужно конвертировать в строку.
with open("hello.txt", "w") as file:
    file.write("hello world")

# Теперь дозапишем в этот файл еще одну строку:
with open("hello.txt", "a") as file:
    file.write("\ngood bye, world")

# Еще один способ записи в файл представляет стандартный метод print()
with open("hello.txt", "a") as hello_file:
    print("Hello, world", file=hello_file)

# Чтение файла
# Для чтения файла он открывается с режимом r (Read), и затем мы можем считать его содержимое различными методами:
#       readline(): считывает одну строку из файла
#       read(): считывает все содержимое файла в одну строку
#       readlines(): считывает все строки файла в список
with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="")
# Несмотря на то, что мы явно не применяем метод readline() для чтения каждой строки, но в при переборе файла этот метод
# автоматически вызывается для получения каждой новой строки. Поэтому в цикле вручную нет смысла вызывать метод readline.
# И поскольку строки разделяются символом перевода строки "\n", то чтобы исключить излишнего переноса на другую строку
# в функцию print передается значение end="".

# явным образом вызовем метод readline() для чтения отдельных строк:
with open("hello.txt", "r") as file:
    str1 = file.readline()
    print(str1, end="")
    str2 = file.readline()
    print(str2)

# readline можно использовать для построчного считывания файла в цикле while:
with open("hello.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()

# Если файл небольшой, то его можно разом считать с помощью метода read():
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

# И также применим метод readlines() для считывания всего файла в список строк:
with open("hello.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
    print(str2)

# При чтении файла мы можем столкнуться с тем, что его кодировка не совпадает с ASCII. В этом случае мы явным образом
# можем указать кодировку с помощью паоаметра encoding:
filename = "hello.txt"
with open(filename, encoding="utf8") as file:
    text = file.read()

# небольшой скрипт, в котором будет записывать введенный пользователем массив строк
# и считывать его обратно из файла на консоль:
#
# имя файла
FILENAME = "messages.txt"
# определяем пустой список
messages = list()

for i in range(4):
    message = input("Введите строку " + str(i + 1) + ": ")
    messages.append(message + "\n")

# запись списка в файл
with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)

# считываем сообщения из файла
print("Считанные сообщения")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")

