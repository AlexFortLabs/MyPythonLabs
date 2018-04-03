# Фоматирование дат и времени
# Для форматирования объектов date и time в обоих этих классах предусмотрен метод strftime(format). Этот метод
# принимает только один параметр, указывающий на формат, в который нужно преобразовать дату или время.

# Для определения формата мы можем использовать один из следующих кодов форматирования:
#       %a: аббревиатура дня недели. Например, Wed - от слова Wednesday (по умолчанию используются английские наименования)
#       %A: день недели полностью, например, Wednesday
#       %b: аббревиатура названия месяца. Например, Oct (сокращение от October)
#       %B: название месяца полностью, например, October
#       %d: день месяца, дополненный нулем, например, 01
#       %m: номер месяца, дополненный нулем, например, 05
#       %y: год в виде 2-х чисел
#       %Y: год в виде 4-х чисел
#       %H: час в 24-х часовом формате, например, 13
#       %I: час в 12-ти часовом формате, например, 01
#       %M: минута
#       %S: секунда
#       %f: микросекунда
#       %p: указатель AM/PM
#       %c: дата и время, отформатированные под текущую локаль
#       %x: дата, отформатированная под текущую локаль
#       %X: время, форматированное под текущую локаль

# Используем различные форматы:
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d"))             # 2018-03-28
print(now.strftime("%d/%m/%Y"))             # 28/03/2018
print(now.strftime("%d/%m/%y"))             # 28/03/18
print(now.strftime("%d %B %Y (%A)"))        # 28 March 2018 (Wednesday)
print(now.strftime("%d/%m/%y %I:%M"))       # 28/03/18 12:50

# по умолчанию используются английские наименования. Если мы хотим использовать текущую локаль,
# то мы можем ее предварительно установить с помощью модуля locale:
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "")

now = datetime.now()
print(now.strftime("%d %B %Y (%A)"))  # 28 März 2018 (Mittwoch)


# Сложение и вычитани дат и времени

# Нередко при работе с датами возникает необходимость добавить к какой-либо дате определенный промежуток времени или,
# наоборот, вычесть некоторый период. И специально для таких операций в модуле datetime определен класс timedelta.
# Фактически этот класс определяет некоторый период времени.

# Для определения промежутка времени можно использовать конструктор timedelta:
#       timedelta([days] [, seconds] [, microseconds] [, milliseconds] [, minutes] [, hours] [, weeks])
# В конструктор мы последовательно передаем дни, секунды, микросекунды, миллисекунды, минуты, часы и недели.
# Определим несколько периодов:
from datetime import timedelta

three_hours = timedelta(hours=3)
print(three_hours)  # 3:00:00
three_hours_thirty_minutes = timedelta(hours=3, minutes=30)  # 3:30:00

two_days = timedelta(2)  # 2 days, 0:00:00
print(two_days)
two_days_three_hours_thirty_minutes = timedelta(days=2, hours=3, minutes=30)  # 2 days, 3:30:00
print(two_days_three_hours_thirty_minutes)

# Используя timedelta, мы можем складывать или вычитать даты. Например, получим дату, которая будет через два дня:
from datetime import timedelta, datetime

now = datetime.now()
print(now)  # 2018-03-28 12:59:56.609327
two_days = timedelta(2)
in_two_days = now + two_days
print(in_two_days)  # 2018-03-30 12:59:56.609327

# Или узнаем, сколько было времени 10 часов 15 минут назад, то есть фактически нам надо вычесть
# из текущего времени 10 часов и 15 минут:
from datetime import timedelta, datetime

now = datetime.now()
till_ten_hours_fifteen_minutes = now - timedelta(hours=10, minutes=15)
print(till_ten_hours_fifteen_minutes)       # 2018-03-28 02:47:28.344364

# Свойства timedelta
# Класс timedelta имеет несколько свойств, с помощью которых мы можем получить временной промежуток:
#       days: возвращает количество дней
#       seconds: возвращает количество секунд
#       microseconds: возвращает количество микросекунд
# Кроме того, метод total_seconds() возвращает общее количество секунд, куда входят и дни, и собственно секунды, и микросекунды.
# Например, узнаем какой временной период между двумя датами:
from datetime import timedelta, datetime

now = datetime.now()
twenty_two_may = datetime(2017, 3, 28)
period = twenty_two_may - now
print("{} дней  {} секунд   {} микросекунд".format(period.days, period.seconds, period.microseconds))
# -366 дней  34703 секунд   94904 микросекунд

print("Всего: {} секунд".format(period.total_seconds()))
# Всего: -31587696.905096 секунд


# Сравнение дат
# Также как и строки и числа, даты можно сравнивать с помощью стандартных операторов сравнения:
from datetime import datetime

now = datetime.now()
deadline = datetime(2018, 4, 10)
if now > deadline:
    print("Срок сдачи проекта прошел")
elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
    print("Срок сдачи проекта сегодня")
else:
    period = deadline - now
    print("Осталось {} дней".format(period.days))
