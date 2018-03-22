import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', help='Путь к директории, в которой лежит коллекция документов', required=True, dest='dir')
parser.add_argument('--model', help='Путь к файлу, в который сохраняется модель', required=True)
parser.add_argument('--lc', help='Привести тексты к lowercase', action='store_const', const=True)
namespace = parser.parse_args()

files = os.listdir(namespace.dir)

def colibrate(fileread):
    filewrite = open(namespace.model, 'w', encoding='utf-8')
    fileread = open(fileread, 'r', encoding='utf-8')
    dictionary_stat = {}
    for line in fileread:
        reg = re.compile('[^A-Za-zА-Яа-яё]')
        tmp_line = reg.sub(' ', line)
        if namespace.lc:
            tmp_line = tmp_line.lower()
        tmp_line = tmp_line.split()
        for i in range(len(tmp_line) - 1):
            pair = tmp_line[i] + ' ' + tmp_line[i + 1]
            dictionary_stat[pair] = dictionary_stat[pair] + 1 if pair in dictionary_stat else 1
    for key in dictionary_stat:
        filewrite.write(str(str(key) + ' ' + str(dictionary_stat[key]) +'\n'))
    fileread.close()
    filewrite.close()

for i in files:
    filename, file_extension = os.path.splitext(i)
    if file_extension == '.txt':
        temp = str(os.getcwd() + '/texts/' + str(i))
        print(temp)
        colibrate(temp)
