# coding: utf-8

import re
import os
import argparse

# Командный интерфейс
parser = argparse.ArgumentParser()
parser.add_argument('--input-dir',
                    help='Путь к директории с коллекцией документов',
                    required=True,
                    dest='dir')

parser.add_argument('--model',
                    help='Путь к файлу, в который сохраняется модель',
                    required=True)

parser.add_argument('--lc',
                    help='Привести тексты к lowercase',
                    action='store_const',
                    const=True)

namespace = parser.parse_args()


# Функция, обрабатывающая данный текст
# На вход подается адрес файла с текстом
def train(fileread):
    # Файл для записи статистики
    filewrite = open(namespace.model, 'tw', encoding='utf-8')
    # Файл с текстом
    fileread = open(fileread, 'r', encoding='utf-8')

    # Словарь, хранящий статистику
    dictionary_stat = {}
    # Достаем часть текста
    for line in fileread:
        # Разрешенные символы
        reg = re.compile('[^A-Za-zА-Яа-яё]')
        # Удаляем лишние символы (оставляем нужные)
        tmp_line = reg.sub(' ', line)

        if namespace.lc:  # Если в консоли попросили убрать заглавные буквы
            tmp_line = tmp_line.lower()

        tmp_line = tmp_line.split()

        # Проходим по куску текста
        for i in range(len(tmp_line) - 1):
            # 2 подряд идущие слова объединяем в словосочетание,
            # записываем их в словарь
            pair = tmp_line[i] + ' ' + tmp_line[i + 1]
            # Учитываем повторяющиеся словосочетания
            dictionary_stat[pair] = dictionary_stat[pair] + 1 \
                if pair in dictionary_stat else 1

    for key in dictionary_stat:  # Запись в файл полученной статистики
        filewrite.write(str(str(key) + ' ' + str(dictionary_stat[key]) + '\n'))

    # Закырваем файлы
    fileread.close()
    filewrite.close()


def view_folder(path):
    # если файл - папка
    if os.path.isdir(path):
        # Путь к текущей директории
        link = os.path.normpath(path)
        # Список фалов в текущей директории
        files = os.listdir(path)

        # Рассматриваем каждый файл в директории
        for i in files:
            # открываем папку в текущей директории
            view_folder(link + '/' + str(i))

    # Разделяем имя файла на 2 части: заголовок и формат
    filename, file_extension = os.path.splitext(path)
    # Если .тхт, то обрабатываем его
    if file_extension == '.txt':
        # Обрабатываемый файл
        file = str(os.path.normpath(path))
        train(file)


view_folder(namespace.dir)
