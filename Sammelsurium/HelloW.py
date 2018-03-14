# Вывод сообщения на консоль
print("Hello Python from Visual Studio!", " in 2018") # Вывод сообщения на консоль

name = input("Введите имя: ")
print("Привет", name)

user_id = "12tomsmith438"  # тип str
print(user_id)
print(type(user_id))  # <class 'str'>
 
user_id = 234  # тип int
print(user_id)
print(type(user_id))  # <class 'int'>

# Целочисленное деление двух чисел:
print(7 / 2)  # 3.5
print(7 // 2)  # 3

print(6 ** 2)  # Возводим число 6 в степень 2. Результат - 36

print(7 % 2)  # Получение остатка от деления числа 7 на 2. Результат - 1

x = 0b101   # 101 в двоичной системе равно 5
a = 0o11    # 11 в восьмеричной системе равно 9
y = 0x0a    # a в шестнадцатеричной системе равно 10

x = 0b101   # 5
y = 0x0a    # 10
z = x + y   # 15
print("{0} in binary {0:08b}   in hex {0:02x} in octal {0:02o}".format(z))
