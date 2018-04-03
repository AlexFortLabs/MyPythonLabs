# Строка
# представляет последовательность символов в кодировке Unicode. И мы можем обратиться к отдельным символам строки по индексу в квадратных скобках:
string = "hello world"
c0 = string[0]  # h
print(c0)
c6 = string[6]  # w
print(c6)

# если мы попытаемся обратиться к индексу, которого нет в строке, то мы получим исключение IndexError
#c11 = string[11]  # ошибка IndexError: string index out of range
#print(c11)

# индекс -1 будет представлять последний символ, а -2 - предпоследний символ и так далее:
string = "hello world"
c1 = string[-1]  # d
print(c1)
c5 = string[-5]  # w
print(c5)

# строка - это неизменяемый (immutable) тип, поэтому если мы попробуем изменить какой-то отдельный символ строки, то мы получим ошибку:
#string = "hello world"
#string[1] = "R"

# мы можем получить из строки не только отдельные символы, но и подстроку. Для этого используется следующий синтаксис:
#       string[:end]: извлекается последовательность символов начиная с 0-го индекса по индекс end
#       string[start:end]: извлекается последовательность символов начиная с индекса start по индекс end
#       string[start:end:step]: извлекается последовательность символов начиная с индекса start по индекс end через шаг step
string = "hello world"

# с 0 до 5 символа
sub_string1 = string[:5]
print(sub_string1)  # hello

# со 2 до 5 символа
sub_string2 = string[2:5]
print(sub_string2)  # llo

# со 2 по 9 символ через один символ
sub_string3 = string[2:9:2]
print(sub_string3)  # lowr

# с помощью функции ord() мы можем получить числовое значение для символа в кодировке Unicode:
print(ord("A"))     # 65

# Для получения длины строки можно использовать функцию len():
string = "hello world"
length = len(string)
print(length)   # 11

# С помощью выражения term in string можно найти подстроку term в строке string. Если подстрока найдена,
# то выражение вернет значение True, иначе возвращается значение False:
string = "hello world"
exist = "hello" in string
print(exist)  # True

exist = "sword" in string
print(exist)  # False

# Перебор строки
# С помощью цикла for
string = "hello world"
for char in string:
    print(char)

