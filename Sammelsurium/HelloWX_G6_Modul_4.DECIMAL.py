# При работе с числами с плавающей точкой (то есть float) мы сталкиваемся с тем, что в результате вычислений
# мы получаем не совсем верный результат:
number = 0.1 + 0.1 + 0.1
print(number)       # 0.30000000000000004
# Проблему может решить использование функции round(), которая округлит число. Однако есть и другой способ,
# который заключается в использовании встроенного модуля decimal. Для его применения нам надо создать его объект с
# помощью конструктора. В конструктор передается строковое значение, которое представляет число. После этого объект
# Decimal можно использовать в арифметических операциях:
from decimal import Decimal

number = Decimal("0.1")
number = number + number + number
print(number)  # 0.3

# В операциях с Decimal можно использовать целые числа:
number = Decimal("0.1")
number = number + 2
# Однако нельзя смешивать в операциях дробные числа float и Decimal:
#number = Decimal("0.1")
#number = number + 0.1   # здесь возникнет ошибка
# С помощью дополнительных знаков мы можем определить, сколько будет символов в дробной части числа:
number = Decimal("0.10")
number = 3 * number
print(number)       # 0.30
# "0.10" определяет два знака в дробной части, даже если последние символы будут представлять ноль.
# Соответственно "0.100" представляет три знака в дробной части.

# Округление чисел
# Объекты Decimal имеют метод quantize(), который позволяет округлять числа. В этот метод в качестве первого аргумента
# передается также объект Decimal, который указывает формат округления числа:
from decimal import Decimal

number = Decimal("0.444")
number = number.quantize(Decimal("1.00"))
print(number)  # 0.44

number = Decimal("0.555678")
print(number.quantize(Decimal("1.00")))  # 0.56

number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))  # 1.00
# Используемая строка "1.00" указывает, что округление будет идти до двух знаков в дробной части.

# По умолчанию округление описывается константой ROUND_HALF_EVEN, при котором число округляется в большую сторону,
# если оно нечетное, а предыдущее перед ним больше 4. Например:
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_DOWN, ROUND_05UP, ROUND_CEILING, ROUND_FLOOR

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))  # 10.02

number = Decimal("10.035")
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))  # 10.04

# Данное поведение при округлении, возможно, не всем покажется желательным, и в этом случае его можно переопределить,
# использовав одну из следующих констант:
#       ROUND_HALF_UP: округляет число в сторону повышения, если после него идет число 5 или выше
#       ROUND_HALF_DOWN: округляет число в сторону повышения, если после него идет число больше 5
number = Decimal("10.026")
print(number.quantize(Decimal("1.00"), ROUND_HALF_DOWN))  # 10.03

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_HALF_DOWN))  # 10.02

#       ROUND_05UP: округляет только 0 до единицы, если после него идет 5
number = Decimal("10.005")
print(number.quantize(Decimal("1.00"), ROUND_05UP))  # 10.01

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_05UP))  # 10.02

#       ROUND_CEILING: округляет число в большую сторону вне зависимости от того, какое число идет после него
number = Decimal("10.021")
print(number.quantize(Decimal("1.00"), ROUND_CEILING))  # 10.03

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_CEILING))  # 10.03

#       ROUND_FLOOR: не округляет число вне зависимости от того, какое число идет после него
number = Decimal("10.021")
print(number.quantize(Decimal("1.00"), ROUND_FLOOR))  # 10.02

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_FLOOR))  # 10.02