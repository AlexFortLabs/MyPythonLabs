#! Программа Банковский счет
# V1 - so importieren wir unser Modul account (File account.py - also gleichnaemig)
import account
# Hier noch weitere Import-Varianten:
# V2 - importiere Modul mid umordnung des Variablenbereich
# import account as acc
# V3 - importiere Funktional aus Modul per FROM
# from account import calculate_income
# V4 - importiere alles an Funktionen aus Modul *
# from    account import *

def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счета в месяцах: "))

    result = account.calculate_income(rate, money, period)
    # oder für V2 ist das dann:
    # result = acc.calculate_income(rate, money, period)

    # oder für V3 ist das dann:
    # result = calculate_income(rate, money, period)

    # oder für V4 ist das dann:
    # result = calculate_income(rate, money, period)

    # Achtung! Variante 3 und 4 übertragen die Variablen aus Modulen in Globeles Umfeld das ist Fehleranfeliger
    # wenn du mit gleichen Bezeichnungen für Funktionene und Variablen arbeites.
    print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n",
          "Период: ", period, "\n", "Сумма на счете в конце периода: ", result)

# В файле HelloW7_Module.py также можно сделать проверку на то, является ли модуль главным (хотя в прицнипе это необязательно):
if __name__ == "__main__":
    main()