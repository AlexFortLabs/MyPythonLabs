# Операции сравнения
a = 5
b = 6
result = 5 == 6  # сохраняем результат операции в переменную
print(result)  # False - 5 не равно 6
print(a != b)  # True
print(a > b)  # False - 5 меньше 6
print(a < b)  # True
 
bool1 = True
bool2 = False
print(bool1 == bool2)  # False - bool1 не равно bool2

# Логические операции
# Если в одном выражении одновременно используется несколько или даже все логические операторы, 
# то следует учитывать, что они  имеют разные приоритеты. 
# Вначале выполняется оператор NOT, затем оператор AND, а в конце оператор OR

# AND
age = 22
weight = 58
result = age > 21 and weight == 58
print(result)  # True

# OR - Возвращает True, если хотя бы одно из выражений равно True
age = 22
isMarried = False
result = age > 21 or isMarried
print(result)  # True, так как выражение age > 21 равно True

# NOT - Возвращает True, если выражение равно False
age = 22
isMarried = False
print(not age > 21)  # False
print(not isMarried)  # True

age = 22
isMarried = False
weight = 58
result = weight == 58 or isMarried and not age > 21  # True
print(result)

# Для переопределения порядка вычислений мы можем использовать скобки:
age = 22
isMarried = False
weight = 58
result = (weight == 58 or isMarried) and not age > 21  # False
print(result)