# Программа подсчета слов
# ! Программа подсчета слов в файле
import os


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words
# Здесь в функции get_words() производится начальная сегментация текста на слова. Пи этом все пунктуационные знаки
# удаляются, а переводы стоки заменяется на пробелы. Затем происходит разбитие текста на слова.
# В качестве разделителя по умолчанию применяется пробел.

def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict
# в функции get_words_dict() получаем словарь из слов, где ключ - это уникальное слово, а значение - количество
# вхождений данного слова в тексте.

#В функции main осуществляется ввод пути к файлу и вызов выше определенных функций, а также вывод все статистики.
def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print("Кол-во слов: %d" % len(words))
        print("Кол-во уникальных слов: %d" % len(words_dict))
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()
