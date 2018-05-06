"""
coding: utf-8
Генератор текстов
Павлов Дмитрий
МФТИ 2018
Ревью №1
Версия №0.2.0
"""

import argparse
import random
import json

# Командный интерфейс
parser = argparse.ArgumentParser(description='Генератор текстов. Если модель'
                                             'не создана, то запустить'
                                             'train.py.')
parser.add_argument('--length',
                    type=int,
                    help='Количество слов в сгенерированном тексте,'
                         'например 50.',
                    required=True)

parser.add_argument('--model',
                    help='Путь к файлу, из которого загружается модель.'
                         'Модель - файл со статистикой, полученной после'
                         'обучения.',
                    required=True)

parser.add_argument('--seed',
                    help='Первое слово. Если не указано,'
                         'будет выбрано случайное.')

parser.add_argument('--output',
                    help='Файл, в который будет записан'
                         'сгенерированный текст.')


def find_next_word(current_word, model):
    """Функция на основе модели выдает слово,
    которое наиболее подходит для данного

    param: current_word - данное слово
    param: model - словарь с моделью в виде
    [слово, слово]: сколько раз встретилось

    Возвращает слово, которое будет продоллжением данного или None,
    если нет продолжения"""

    # Кандидаты на искомое слово,
    # Список, хранящий словосочетания, каждое словосочетание будет встречаться
    # в списке столько раз, сколько оно встречалось в прочитаных текстах
    candidats = []

    # Перебираем ключи в словаре, ищем словосочетания,
    # у которых первый элемент = current_word
    for key in model:
        # Проверка, если первое слово в словосочетанни = current_word,
        # то это словосочетание - кандидат
        if key[0] == current_word:
            tmp = [key * model[key]]
            candidats.extend(tmp)

    # Если кандидаты не найдены, то генерация завершается
    if len(candidats) == 0:
        # Флаг, что алгоритм зашел в тупик
        return None

    # Вибираем наиболее подходящую пару из кандидатов
    word = random.choice(candidats)
    # Если пара такая, что после current_word есть слово,
    # то оно будет продолжением
    if len(word) > 1:
        return word[1]
    # Если пара такая, что после current_word нет слова,
    # то алгоритм зашел в тупик
    else:
        return None


def generate(len_text, seed, model):
    """Функция, генерирующая текст

    param: len_text - максимальная длина генерируемого текста
    param: seed - слово с которого должен начаться текст
    param: pairs - словарь с моделью

    Возвращает сгенерированный текст"""

    # Список для текста, который выдаст функция
    text = []

    # Если первоначальное слово задано, то строим текст начиная с него
    if seed is not None:
        # Будет список из пар, у которых первый элемент=seed или пустой список
        word = list(filter(lambda x: x[0] if x[0] == seed else None,
                           model.keys()))

        # Проверка, что слово нашлось
        if (len(word) > 0):
            # Получили список из пар, у которых первый элемент = seed
            word = word[0][0]
        # Если не нашли то исключение
        else:
            raise SystemError('Seed word does not exist')
    # Если не задано первое слово, то выберем рандомное из списка
    else:
        # в pairs ключ - пара (слово, слово), выбираем рандоменую пару,
        # а в ней первый элемент
        word = (random.choice(list(model.keys())))[0]

    # В цикле для i-го слова буем искать i + 1 при помощи полученной статистики
    for i in range(len_text):
        text.append(word)

        # Определяем подходящее слово
        word = find_next_word(word, model)

        # Если подходящего слова нет, значит алгоритм зашел в тупик
        if word is None:
            return ' '.join(text)

    return ' '.join(text)


if __name__ == '__main__':
    # Парсинг аргументов
    namespace = parser.parse_args()

    # Словарь со статистикой
    model_tmp = {}
    model = {}

    # Получаем статистику из файла
    with open(namespace.model, 'r') as file:
        # Открываем результаты обработки текстов,
        # Заносим эти данные в словарь
        model_tmp = json.load(file)

    # Преобразуем словарь к виду "(слово, слово) : статистика"
    for key in model_tmp:
        model[tuple(key.split())] = model_tmp[key]
    # Генерируем текст
    text = generate(namespace.length, namespace.seed, model)

    # Если указано в какой файл записать текст, то запишем его туда
    if namespace.output is not None:
        # Указанный файл
        with open(namespace.output, 'w') as file:
            # Запись в файл
            file.write(text)
    # Если не указано в какой файл записать текст, то выведем его
    else:
        print(text)
