def say_hello(name):
    print("Hello,", name)


say_hello("Tom")
say_hello("Bob")
say_hello("Alice")

# Значения по умолчанию
def display_info(name, age=10):
    print("Name:", name, "\t", "Age:", age)


display_info("Tom", 22)                 #Name: Tom 	 Age: 22
display_info("Petja")                   #Name: Petja 	 Age: 10
display_info(age=25, name="Vasja")      # Name: Vasja 	 Age: 25

# Возвращение результата
def exchange(usd_rate, money):
    result = round(money / usd_rate, 2)
    return result


result1 = exchange(60, 30000)
print(result1)
result2 = exchange(56, 30000)
print(result2)
result3 = exchange(65, 30000)
print(result3)

# В Python функция может возвращать сразу несколько значений:
def create_default_user():
    name = "Tom"
    age = 33
    return name, age

user_name, user_age = create_default_user()
print("Name:", user_name, "\t Age:", user_age)


# Funktion MAIN
# В программе может быть определено множество функций. И чтобы всех их упорядочить, хорошей практикой считается
# добавление специальной функции main, в которой потом уже вызываются другие функци

def main():
    say_hello("Tom")
    usd_rate = 56
    money = 30000
    result = exchange(usd_rate, money)
    print("К выдаче", result, "долларов")

# Вызов функции main
main()