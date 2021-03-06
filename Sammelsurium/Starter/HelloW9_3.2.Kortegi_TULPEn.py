# Кортеж (tuple) представляет последовательность элементов, которая во многом похожа на список
# за тем исключением, что кортеж является неизменяемым (immutable) типом.
# создания кортежа используются круглые скобки
user = ("Tom", 23)
user = "Tom", 23
user = ("Tom",)

# создания кортежа из списка можно передать список в функцию tuple()
users_list = ["Tom", "Bob", "Kate"]
users_tuple = tuple(users_list)
print(users_tuple)      # ("Tom", "Bob", "Kate")

# Обращение к элементам в кортеже происходит также, как и в списке по индексу.
# Индексация начинается также с нуля при получении элементов с начала списка и с -1 при получении элементов с конца списка:
users = ("Tom", "Bob", "Sam", "Kate")
print(users[0])  # Tom
print(users[2])  # Sam
print(users[-1])  # Kate

# получим часть кортежа со 2 элемента по 4
print(users[1:4])  # ("Bob", "Sam", "Kate")

# Особенно удобно использовать кортежи, когда необходимо возвратить из функции сразу несколько значений.
# Когда функция возвращает несколько значений, фактически она возвращает в кортеж:
def get_user():
    name = "Tom"
    age = 22
    is_married = False
    return name, age, is_married


user = get_user()
print(user[0])  # Tom
print(user[1])  # 22
print(user[2])  # False

# получить длину кортежа:
user = ("Tom", 22, False)
print(len(user))        # 3

# ---------- Перебор кортежей
# Для перебора кортежа можно использовать стандартные циклы for и while.
# С помощью цикла for:
user = ("Tom", 22, False)
for item in user:
    print(item)

# С помощью цикла while:
user = ("Tom", 22, False)

i = 0
while i < len(user):
    print(user[i])
    i += 1

# ---------- проверить наличие элемента в кортеже:
user = ("Tom", 22, False)
name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")

# ---------- Сложные кортежи
# Один кортеж может содержать другие кортежи в виде элементов
countries = (
    ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2), ("Marsel", 1.6)))
)

for country in countries:
    countryName, countryPopulation, cities = country
    print("\nCountry: {}  population: {}".format(countryName, countryPopulation))
    for city in cities:
        cityName, cityPopulation = city
        print("City: {}  population: {}".format(cityName, cityPopulation))
