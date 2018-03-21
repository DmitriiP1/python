import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', '--input-dir', help='Путь к директории, в которой лежит коллекция документов')
parser.add_argument('--model', help='Путь к файлу, в который сохраняется модель', required=True)
parser.add_argument('--lc', help='Привести тексты к lowercase', action='store_const', const=True)
namespace = parser.parse_args()

files = os.listdir(namespace.dir)
texts = list(filter(lambda  x: x.endswith('.txt'), files))
direct = namespace.dir + '\\' + texts[0]

def colibrate():
    fileread = open('read.txt', 'r')
    filewrite = open('write.txt', 'w')
    dictionary_stat = {}
    for line in fileread:
        reg = re.compile('[^A-Za-zА-Яа-яtё]')
        tmp_line = reg.sub(' ', line)
        if namespace.lc:
            tmp_line = tmp_line.lower()
        tmp_line = tmp_line.split()
        for i in range(len(tmp_line) - 1):
            pair = tmp_line[i] + ' ' + tmp_line[i + 1]
            dictionary_stat[pair] = dictionary_stat[pair] + 1 if pair in dictionary_stat else 1

    for i in dictionary_stat:
        filewrite.write(str(str(i) + ' ' + str(dictionary_stat[i]) +'\n'))
    fileread.close()
    filewrite.close()


colibrate()
