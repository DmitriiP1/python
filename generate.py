"""
coding: utf-8
Генератор текстов
Павлов Дмитрий
МФТИ 2018
Ревью №1
Версия №0.1.3
"""

import argparse
import random
import json
from functools import reduce

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


def find_next_word(current_word, pairs):
    """Функция на основе модели выдает слово,
   которое наиболее подходит для данного

   param: current_word - данное слово
   param: dictionary_stat - словарь с моделью

   Возвращает слово, которое будет продоллжением данного или None,
    если нет продолжения"""
    # --------------------------------------------------- #

    # Кандидаты на искомое слово,
    # Список, хранящий словосочетания
    candidats = []

    # Перебираем ключи в словаре, ищем кандидатов и записываем статистику
    for key in pairs:
        # Проверка, если первое слово в словосочетанни = данному,
        # то это словосочетание - кандидат
        if key[0] == current_word:
            tmp = [key * pairs[key]]
            candidats.extend(tmp)

    # Если кандидаты не найдены, то генерация завершается
    if len(candidats) == 0:
        # Флаг, что алгоритм зашел в тупик
        return None

    word = random.choice(candidats)
    if len(word) == 1:
        return None
    return word[1]


def generate(len_text, seed, pairs):
    """Функция, генерирующая текст

   param: len_text - максимальная длина генерируемого текста
   param: dictionary_stat - словарь с моделью
   param: seed - слово с которого начинается текст

   Возвращает сгенерированный текст"""
    # ------------------------------------------------ #

    # Список для текста, который выдаст функция
    text = []
    word = ''
    # Если не задано первое слово, то выберем рандомное из списка
    if seed is None:
        word = (random.choice(list(pairs.keys())))[0]
    # Если первоначальное слово задано, то строим текст начиная с него
    else:
        word = list(filter(lambda x: x[0] if x[0] == seed else None,
                           pairs.keys()))[0][1]
        # В словаре нет seed
        if word is None:
            # Если не нашли то исключение
            raise SystemError(256)
        text.append(seed)
        len_text -= 1
    # В цикле для i-го слова буем искать i + 1 при помощи полученой статистики

    for i in range(len_text):
        text.append(word)

        # Определяем подходящее слово
        word = find_next_word(word, pairs)
        # Если подходящего слова нет, значит алгоритм зашел в тупик
        if word is None:
            return ' '.join(text)
    return ' '.join(text)


if __name__ == '__main__':
    # Парсинг аргументов
    namespace = parser.parse_args()

    # Словарь со статистикой
    pairs_tmp = {}
    pairs = {}
    with open(namespace.model, 'r') as file:
        # Открываем результаты обработки текстов,
        # Заносим эти данные в словарь
        pairs_tmp = json.load(file)

    for key in pairs_tmp:
        pairs[tuple(key.split())] = pairs_tmp[key]

    # Генерируем текст
    text = generate(namespace.length, namespace.seed, pairs)
    # Если указано в какой файл записать текст, то запишем его туда
    if namespace.output is not None:
        # Указанный файл
        with open(namespace.output, 'w') as file:
            # Запись в файл
            file.write(text)

    # Если не указано в какой файл записать текст, то выведем его
    else:
        print(text)
