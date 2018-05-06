"""
coding: utf-8
Создание модели по набору текстов
Павлов Дмитрий
МФТИ 2018
Ревью №1
Версия №0.2.0
"""

import re
import os
import argparse
import json
from collections import defaultdict
from collections import Counter

# Командный интерфейс
parser = argparse.ArgumentParser(description='Создание модели. Модель нужна'
                                             'для генерации текстов'
                                             'программой generate.py.')
parser.add_argument('--input-dir',
                    help='Путь к директории с коллекцией .txt документов.'
                         'По этим текстам программа обучится создавть свои'
                         'тексты.',
                    required=True,
                    dest='dir')

parser.add_argument('--model',
                    help='Путь к файлу, в который сохраняется модель.'
                         'Модель нужна для сохранения статистики, полученной'
                         'после обучения.',
                    required=True)

parser.add_argument('--lc',
                    help='Привести тексты к нижнему регистру.',
                    action='store_const',
                    const=True)


def train(file_for_train, lowercase, model_dict, used):
    """ Функция, дополняющая модель по данным из текста
    Возвращает модель, дополненную новыми данными

    param: file_for_train -файл с текстом по которому будет обучаться программа
    param: lowercase - переменная, отвечающая за приведение слов, сохраняемых
    в модели, к нижнему регистру
    param: model_dict - словарь, ключ - пары слов, значение - статистика
    param: used - список слов, которые есть в model_dict"""

    with open(file_for_train, 'r', encoding='utf-8') as file_for_train:
        # Достаем часть текста
        for line in file_for_train:
            # Разрешенные символы
            reg = re.compile('[^A-Za-zА-Яа-яё]')
            # Удаляем лишние символы (оставляем нужные)
            line = reg.sub(' ', line)

            # Если необходимо убрать заглавные буквы
            if lowercase:
                line = line.lower()

            # Разобьем кусок текста на слова
            line = line.split()

            # Список с новыми словосочетаниями
            new_pairs = []

            # Проходим по куску текста
            for current_word in range(len(line) - 1):
                # 2 подряд идущие слова объединяем
                # в словосочетание, записываем их в словарь
                pair = line[current_word] + ' ' + line[current_word + 1]
                new_pairs.append(pair)
                used.append(line[current_word])

            # Если слово последнее, и не встречалось раньше, то пара
            # выглядит как (слово, None) то есть состоит из одного элемента
            if line and line[-1] not in used:
                pair = line[-1]
                new_pairs.append(pair)

            # превращаем new_pairs в словарь
            new_pairs = Counter(new_pairs)

            # Слияние словаря с моделью и нового словаря
            for key in new_pairs:
                model_dict[key] += new_pairs[key]

    return model_dict


def get_model(directory, lowercase):
    """ Поиск .txt файлов в директории
    Возвращает список пар слов

    param: directory - директория с файлами для обучения
    param: lowercase - переменная, отвечающая за приведение слов, сохраняемых
       в модели, к нижнему регистру

    Возвращает словарь: ключ - словосочетание, записанное через пробел,
    значение - сколько раз оно встретилось в текстах"""

    # Словарь с моделью
    model_dict = defaultdict(int)

    # Слова которые есть в model_dict
    used = []

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

                # Обновление модели по данным из текущего файла
                model_dict = train(file, lowercase, model_dict, used)
    return model_dict


if __name__ == '__main__':
    # Парсинг аргументов
    namespace = parser.parse_args()

    # Файл для записи модели
    with open(namespace.model, 'w', encoding='utf-8') as model_file:

        # Список пар слов преобразуется в словарь
        # Ключ - пара слов, значение - сколько раз встречалась эта пара
        model_dict = get_model(namespace.dir, namespace.lc)
        # Запись в файл словаря со статистикой в модель
        json.dump(model_dict, model_file)
