# coding: utf-8

from random import randint
import argparse

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

# Открываем результаты обработки текстов,
# Заносим эти данные в словарь
# Дальше работаем с файлом путь к которому задана в model
with open(namespace.model, 'r') as file:
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


# Функция выдает слово, которое наиболее подходит для данного
# (через частоту встречающихся словосочетаний)
def find_next_word(current_word, dictionary_stat):
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
        return 'WRONG'

    # Определение наиболее подходящего кандидата.
    # Сложим все значения в словаре, полученные по ключам(=найденные кандидаты)
    # Рандом выдаст некоторое число,
    # учитывая что в списке порядок элементов определен однозначно,
    # можем найти наиболее подходящего кандидадата
    sum = 0
    for word in candidats:
        # Сложим все полученные по ключам значения в словаре
        sum = sum + int(dictionary_stat[word])

    random_int = randint(0, sum - 1)
    for collocation in candidats:
        temp = collocation.split()
        if int(dictionary_stat[collocation]) >= random_int:
            return temp[1]
        random_int = random_int - int(dictionary_stat[collocation])


# Функция, генерирующая текст
# На вход подается число слов в генерируемом тексте
# Выдает список слов в порядке, в котором они должны стоять в тексте
def generate(len_text):
    # Список для текста, который выдаст функция
    text = []

    # Если не задано первое слово, то выберем рандомное из списка
    if namespace.seed is None:
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
    # Если первоначальное слово задано, то строим текст начиная с него
    else:
        flag = False
        # Ищем есть ли seed среди ключей в словаре
        for key in dictionary_stat:
            temp = key.split()
            if temp[0] == namespace.seed:
                # Нашли
                flag = True
        if flag:
            word = namespace.seed
        else:
            # Если не нашли то исключение
            raise SystemError(256)
    # В цикле для i-го слова буем искать i + 1 при помощи полученой статистики
    if word != '':
        for i in range(len_text):
            text.append(word)
            # Определяем подходящее слово
            word = find_next_word(word, dictionary_stat)
            # Если подходящего слова нет, значит алгоритм зашел в тупик
            if word == 'WRONG':
                return text
    return text


# Генерируем текст
text = generate(namespace.length)
# Если указано в какой файл записать сгенерируемый текст, то запишем его туда
if namespace.output is not None:
    # Указанный файл
    file = open(namespace.output, 'w')
    # Запись в файл

    for i in text:
        file.write(str(i) + ' ')
    file.close()
# Если не указано в какой файл записать сгенерируемый текст, то выведем его
else:
    print(' '.join(text))
