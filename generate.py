from random import randint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--length', type=int, help='Длина генерируемой последовательности.',required=True)
parser.add_argument('--model', help='Путь к файлу, из которого загружается модель', required=True)
parser.add_argument('--seed', help='Начальное слово')
parser.add_argument('--output', help='Файл, в который будет записан результат')
namespace = parser.parse_args()

#Открываем результаты обработки текстов, заносим эти данные в словарь
def readinput():
    with open(namespace.model, 'r') as file:
        dictionary_stat = {}
        for line in file:
            line = line.split()
            line_str = str(str(line[0]) + ' ' + str(line[1]))
            dictionary_stat.update({line_str : line[2]})
        file.close()
        return dictionary_stat


def find_next_word(current_word, dictionary_stat):
    candidats = []
    for key in dictionary_stat:
        temp = key.split()
        if temp[0] == current_word:
            candidats.append(key)
    if len(candidats) == 0:
        return 'WRONG'
    sum = 0
    for word in candidats:
        sum = sum + int(dictionary_stat[word])
    random_int = randint(0, sum)
    for candidat in candidats:
        temp = candidat.split()
        if int(dictionary_stat[candidat]) >= random_int:
            return temp[1]
        random_int = random_int - int(dictionary_stat[candidat])


def generate(len_text):
    dictionary_stat = readinput()
    text = []
    if namespace.seed == None:
        start = randint(0, len(dictionary_stat))
        pos = 0
        word = ' '
        for i in dictionary_stat:
            if pos == start:
                word = i.split()
                word = word[0]
                word = str(word)
                break
            pos += 1
    else:
        word = namespace.seed
    for i in range(len_text):
        text.append(word)
        word = find_next_word(word, dictionary_stat)
        if word == 'WRONG':
            return text
    return text


text = []
text = generate(namespace.length)
if namespace.output != None:
    file = open(namespace.output, 'w')
    for i in text:
        file.write(str(i) + ' ')
    file.close()
else:
    print(' '.join(text))