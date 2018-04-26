# coding: utf-8
# Создание модели по набору текстов
# Павлов Дмитрий
# МФТИ 2018
# Ревью №1
# Версия №0.1.0

import re
import os
import argparse
import json

# Глобальная константа
PAIR_FOR_LAST_WORD = '$'

# Командный интерфейс
parser = argparse.ArgumentParser(description='Создание модели. Модель нужна '
                                             'для генерации текстов '
                                             'программой generate.py.')
parser.add_argument('--input-dir',
                    help='Путь к директории с коллекцией .txt документов. '
                         'По этим текстам программа обучится создавть свои '
                         'тексты.',
                    required=True,
                    dest='dir')

parser.add_argument('--model',
                    help='Путь к файлу, в который сохраняется модель. '
                         'Модель нужна для сохранения статистики, полученной '
                         'после обучения.',
                    required=True)

parser.add_argument('--lc',
                    help='Привести тексты к нижнему регистру.',
                    action='store_const',
                    const=True)


namespace = parser.parse_args()


def add_pair(pair, dictionary_stat):
    # Добавляет пару в модель, учитывая повторения

    # pair - добавляемая пара слов

    # dictionary_stat - словарь с моделью
    # ------------------------------------------ #

    if dictionary_stat.setdefault(pair) is None:
        dictionary_stat[pair] = 1
    else:
        dictionary_stat[pair] += 1


def train(file_for_train, lowercase, dictionary_stat):
    # Функция, создающая модель на основе данного текст

    # file_for_train - файл с текстом по которому будет обучаться программа
    # lowercase - переменная, отвечающая за приведение слов, сохраняемых
    # в модели, к нижнему регистру
    # dictionary_stat - словарь с моделью
    # ------------------------------------------------------------------- #

    # Файл с текстом
    with open(file_for_train, 'r', encoding='utf-8') as file_for_train:

        # Достаем часть текста
        for line in file_for_train:
            # Разрешенные символы
            reg = re.compile('[^A-Za-zА-Яа-яё]')
            # Удаляем лишние символы (оставляем нужные)
            line = reg.sub(' ', line)

            # Если в консоли попросили убрать заглавные буквы
            if lowercase:
                line = line.lower()

            line = line.split()

            # Проходим по куску текста
            for i in range(len(line) - 1):
                # 2 подряд идущие слова объединяем в словосочетание,
                # записываем их в словарь
                pair = line[i] + ' ' + line[i + 1]
                add_pair(pair, dictionary_stat)
            if line:
                pair = line[-1] + ' ' + PAIR_FOR_LAST_WORD
                add_pair(pair, dictionary_stat)


def find_txt_files(directory, lowercase, dictionary_stat):
    # Поиск .txt файлов в директории

    # directory - директория с файлами для обучения
    # lowercase - переменная, отвечающая за приведение слов, сохраняемых
    # в модели, к нижнему регистру
    # dictionary_stat - словарь с моделью
    # ---------------------------------------------------------------- #

    # Поиск файлов в директории
    for top, dirs, files in os.walk(directory):
        for i in files:
            # Путь к файлу
            path = str(os.path.join(top, i))

            # Разделяем имя файла на 2 части: заголовок и формат
            filename, file_extension = os.path.splitext(path)
            # Если .тхт, то обрабатываем его
            if file_extension == '.txt':
                # Обрабатываемый файл
                file = str(os.path.normpath(path))
                train(file, lowercase, dictionary_stat)


if __name__ == '__main__':
    # Словарь, хранящий статистику
    dictionary_stat = {}

    open(namespace.model, 'w').close()

    # Файл для записи модели
    with open(namespace.model, 'a+', encoding='utf-8') as model:

        find_txt_files(namespace.dir, namespace.lc, dictionary_stat)

        # Запись в файл созданной модели
        json.dump(dictionary_stat, model)
