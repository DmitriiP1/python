import re
import os
import argparse
#Командный интерфейс
parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', help='Путь к директории, в которой лежит коллекция документов', required=True, dest='dir')
parser.add_argument('--model', help='Путь к файлу, в который сохраняется модель', required=True)
parser.add_argument('--lc', help='Привести тексты к lowercase', action='store_const', const=True)
namespace = parser.parse_args()

#Функция, обрабатывающая данный текст
#На вход подается адрес файла с текстом
def colibrate(fileread):
    filewrite = open(namespace.model, 'tw', encoding='utf-8')#Файл для записи статистики
    fileread = open(fileread, 'r', encoding='utf-8')#Файл с текстом
    dictionary_stat = {}#Словарь, хранящий статистику
    for line in fileread:#Достаем часть текста
        reg = re.compile('[^A-Za-zА-Яа-яё]')#Разрешенные символы
        tmp_line = reg.sub(' ', line)#Удаляем лишние символы (оставляем нужные)
        if namespace.lc:#Если в консоли попросили убрать заглавные буквы
            tmp_line = tmp_line.lower()
        tmp_line = tmp_line.split()
        for i in range(len(tmp_line) - 1):#Проходим по куску текста
            pair = tmp_line[i] + ' ' + tmp_line[i + 1]#2 подряд идущие слова объединяем в словосочетание и записываем в словарь
            dictionary_stat[pair] = dictionary_stat[pair] + 1 if pair in dictionary_stat else 1#Учитываем повторяющиеся словосочетания
    for key in dictionary_stat:#Запись в файл полученной статистики
        filewrite.write(str(str(key) + ' ' + str(dictionary_stat[key]) +'\n'))
    fileread.close()
    filewrite.close()

files = os.listdir(namespace.dir)#список файлов в полученой директории
for i in files:#рассматриваем каждый файл в директории
    filename, file_extension = os.path.splitext(i)#разделяем имя файла на 2 части: заголовок и формат
    if file_extension == '.txt':#если тхт, то обрабатываем его
        temp = str(os.getcwd() + '/texts/' + str(i))#обрабатываемый файл
        #print(temp)#выводим название обработываемого файла
        colibrate(temp)
