# coding: utf-8
# Генератор текстов
# Павлов Дмитрий
# МФТИ 2018
# Ревью №1
# Версия №0.1.0

import argparse
import configparser
import random
import json

# Командный интерфейс
parser = argparse.ArgumentParser(description='Генератор текстов. Если модель '
                                             'не создана, то запустить '
                                             'train.py.')
parser.add_argument('--length',
                    type=int,
                    help='Количество слов в сгенерированном тексте, '
                         'например 50.',
                    required=True)

parser.add_argument('--model',
                    help='Путь к файлу, из которого загружается модель. '
                         'Модель - файл со статистикой, полученной после '
                         'обучения.',
                    required=True)

parser.add_argument('--seed',
                    help='Первое слово. Если не указано, '
                         'будет выбрано случайное.')

parser.add_argument('--output',
                    help='Файл, в который будет записан '
                         'сгенерированный текст.')

namespace = parser.parse_args()


def find_next_word(current_word, dictionary_stat):
    # Функция на основе модели выдает слово,
    # которое наиболее подходит для данного

    # current_word - данное слово
    # dictionary_stat - словарь с моделью

    # Возвращает слово, которое будет продоллжением данного
    # --------------------------------------------------- #

    # Кандидаты на искомое слово,
    # Список в виде словосочетаний(=ключам в словаре),
    candidats = []

    # Перебираем ключи в словаре, ищем кандидатов и записываем статистику
    for key in dictionary_stat:
        # Проверка, если первое слово в словосочетанни = данному,
        # то это словосочетание - кандидат
        if key[0] == current_word:
            candidats.append(key)

    # Если кандидаты не найдены, то генерация завершается
    if len(candidats) == 0:
        # Флаг, что алгоритм зашел в тупик
        return None
    word = (random.choice(candidats))[1]
    return word


def generate(len_text, seed, dictionary_stat):
    # Функция, генерирующая текст

    # len_text - максимальная длина генерируемого текста
    # dictionary_stat - словарь с моделью

    # Возвращает сгенерированный текст
    # ------------------------------------------------ #

    # Список для текста, который выдаст функция
    text = []
    word = ''
    # Если не задано первое слово, то выберем рандомное из списка
    if seed is None:
        word = (random.choice(list(dictionary_stat.keys())))[0]
    # Если первоначальное слово задано, то строим текст начиная с него
    else:
        # В словаре нет seed
        flag = True
        # Ищем есть ли seed среди ключей в словаре
        for key in dictionary_stat:
            if key == seed:
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
            return ' '.join(text)
    return ' '.join(text)


if __name__ == '__main__':
    # Словарь со статистикой
    dictionary_tmp = {}
    dictionary_stat = {}
    with open(namespace.model, 'r') as file:
        # Открываем результаты обработки текстов,
        # Заносим эти данные в словарь
        dictionary_tmp = json.load(file)

    for key in dictionary_tmp:
        dictionary_stat[tuple(key.split())] = dictionary_tmp[key]

    # Чтение конфига
    config = configparser.ConfigParser()
    config.read('settings.ini')
    # letter - символ, который будет показывать, что это слово было
    # последним в тексте и для него нельзя выбрать пару.
    pair_for_last_word = config['settings']['letter']

    # Генерируем текст
    text = generate(namespace.length, namespace.seed, dictionary_stat)
    # Если указано в какой файл записать текст, то запишем его туда
    if namespace.output is not None:
        # Указанный файл
        with open(namespace.output, 'w') as file:
            # Запись в файл
            file.write(text)
            file.close()
    # Если не указано в какой файл записать текст, то выведем его
    else:
        print(text)
