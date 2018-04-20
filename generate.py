# coding: utf-8
# Генератор текстов
# Павлов Дмитрий
# МФТИ 2018
# Ревью №1
# Версия №0.1.0

from random import randint
import argparse
import configparser

# Командный интерфейс
parser = argparse.ArgumentParser()
parser.add_argument('--length',
                    type=int,
                    help='Длина генерируемой последовательности.',
                    required=True)

parser.add_argument('--model',
                    help='Путь к файлу, из которого загружается модель',
                    required=True)

parser.add_argument('--seed',
                    help='Начальное слово')

parser.add_argument('--output',
                    help='Файл, в который будет записан результат')

namespace = parser.parse_args()

# Словарь со статистикой
dictionary_stat = {}

with open(namespace.model, 'r') as file:
    # Открываем результаты обработки текстов,
    # Заносим эти данные в словарь
    # Дальше работаем с файлом путь к которому задана в model

    # Обработка файла,
    # В цикле будем доставать строчки из файла и доавлять их в словарь
    for line in file:
        line = line.split()

        # Строки в файле имеют вид: <слово1>' '<слово2> : статистика
        line_str = str(str(line[0]) + ' ' + str(line[1]))
        # Статистика словосочетания - слово после второго пробела
        dictionary_stat.update({line_str: line[2]})
    # Закрываем файл model
    file.close()


def find_next_word(current_word, dictionary_stat):
    # Функция выдает слово, которое наиболее подходит для данного
    # (через частоту встречающихся словосочетаний)

    # Кандидаты на искомое слово,
    # Список в виде словосочетаний(=ключи в словаре),
    candidats = []

    # Перебираем ключи в словаре, ищем кандидатов и записываем статистику
    for key in dictionary_stat:
        # Проверка, если первое слово в словосочетанни = данному,
        # то это словосочетание - кандидат
        temp = key.split()
        if temp[0] == current_word:
            candidats.append(key)

    # Если кандидаты не найдены, то текст завершается
    if len(candidats) == 0:
        # Флаг, что алгоритм зашел в тупик
        return None

    # Определение наиболее подходящего кандидата.
    # Сложим все значения в словаре, полученные по ключам(=найденные кандидаты)
    # Рандом выдаст некоторое число,
    # учитывая что в списке порядок элементов определен однозначно,
    # можем найти наиболее подходящего кандидадата
    sum_values = 0
    for word in candidats:
        # Сложим все полученные по ключам значения в словаре
        sum_values = sum_values + int(dictionary_stat[word])

    random_int = randint(0, sum_values - 1)
    for collocation in candidats:
        temp = collocation.split()
        if int(dictionary_stat[collocation]) >= random_int:
            return temp[1]
        random_int = random_int - int(dictionary_stat[collocation])


def random_word():
    # Выбирает рандомное слово

    # Seed для слова
    start = randint(0, len(dictionary_stat))
    step = 0
    # Первое слово
    word = ' '
    # Берем элементы из списка, столько, сколько выдал рандом
    for i in dictionary_stat:
        if step == start:
            word = i.split()
            word = word[0]
            word = str(word)
            break
        step += 1
    return word


def generate(len_text, seed):
    # Функция, генерирующая текст
    # На вход подается число слов в генерируемом тексте
    # Выдает список слов в порядке, в котором они должны стоять в тексте

    # Список для текста, который выдаст функция
    text = []
    word = ''
    # Если не задано первое слово, то выберем рандомное из списка
    if seed is None:
        word = random_word()
    # Если первоначальное слово задано, то строим текст начиная с него
    else:
        # В словаре нет seed
        flag = True
        # Ищем есть ли seed среди ключей в словаре
        for key in dictionary_stat:
            temp = key.split()
            if temp[0] == seed:
                word = seed
                # Нашли
                flag = False
        if flag:
            # Если не нашли то исключение
            raise SystemError(256)
    # В цикле для i-го слова буем искать i + 1 при помощи полученой статистики
    for i in range(len_text):
        text.append(word)
        # Определяем подходящее слово
        word = find_next_word(word, dictionary_stat)
        # Если подходящего слова нет, значит алгоритм зашел в тупик
        if word is None or word == pair_for_last_word:
            return text
    return text


if __name__ == '__main__':
    # Чтение конфига
    config = configparser.ConfigParser()
    config.read('settings.ini')
    pair_for_last_word = config['settings']['letter']
    # Генерируем текст
    text = generate(namespace.length, namespace.seed)
    # Если указано в какой файл записать текст, то запишем его туда
    if namespace.output is not None:
        # Указанный файл
        file = open(namespace.output, 'w')
        # Запись в файл
        file.write(' '.join(text))
        file.close()
    # Если не указано в какой файл записать текст, то выведем его
    else:
        print(' '.join(text))
