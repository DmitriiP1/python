# coding: utf-8

from random import randint
import argparse
#Командный интерфейс
parser = argparse.ArgumentParser()
parser.add_argument('--length', type=int, help='Длина генерируемой последовательности.',required=True)
parser.add_argument('--model', help='Путь к файлу, из которого загружается модель', required=True)
parser.add_argument('--seed', help='Начальное слово')
parser.add_argument('--output', help='Файл, в который будет записан результат')
namespace = parser.parse_args()

#Открываем результаты обработки текстов, заносим эти данные в словарь
def readinput():
    with open(namespace.model, 'r') as file:#дальше работаем с файлом путь к которому задана в model
        dictionary_stat = {}#словарь со статистикой словосочетаний
        for line in file:#обработка файла, в цикле будем доставать строчки из файла и доавлять их в словарь
            line = line.split()
            line_str = str(str(line[0]) + ' ' + str(line[1]))#строки в файле имеют вид: <слово1>' '<слово2> : статистика
            dictionary_stat.update({line_str : line[2]})#статистика словосочетания - слово после второго пробела
        file.close()
        return dictionary_stat

#Функция выдает слово, которое наиболее подходит для данного (через частоту встречающихся словосочетаний)
def find_next_word(current_word, dictionary_stat):
    candidats = []#кандидаты на искомое слово, список в виде словосочетаний(=ключи в словаре), затем по словосочетаний найдем статистику
    for key in dictionary_stat: #перебираем ключи в словаре, ищем кандидатов и записываем статистику
        temp = key.split()#временный список чтобы проверить первое слово в словосоечатнии из списка
        if temp[0] == current_word:#проверка, если первое слово в словосочетанни = данному, то это словосочетание - кандидат
            candidats.append(key)
    if len(candidats) == 0:#если кандидаты не найдены, то текст завершается
        return 'WRONG'#"Флаг, что алгоритм зашел в тупик
    #Определение наиболее подходящего кандидата
    #Сложим все значения в словаре, полученные по ключам(=найденные кандидаты)
    #Рандом выдаст некоторое число, учитывая что в списке порядок элементов определен однозначно, можем найти натболее подходящего кандидадата
    sum = 0
    for word in candidats:
        sum = sum + int(dictionary_stat[word])#Сложим все значения в словаре, полученные по ключам(=найденные кандидаты)
    random_int = randint(0, sum)
    for candidat in candidats:
        temp = candidat.split()
        if int(dictionary_stat[candidat]) >= random_int:
            return temp[1]
        random_int = random_int - int(dictionary_stat[candidat])

#Функция, генерирующая текст
#На вход подается число слов в генерируемом тексте
#Функция выдаст список слов в том порядке, в котором они должны стоять в тексте
def generate(len_text):
    dictionary_stat = readinput()#считываем статистику
    text = []#Список для текста который выдаст функция
    if namespace.seed == None:#если не задано первое слово, то выберем рандомное из списка
        start = randint(0, len(dictionary_stat))#некоторое рандомное число
        pos = 0
        word = ' '#первое слово
        for i in dictionary_stat:#будем брать элементы из списка, пока не возьмем их столько, сколько выдал рандом
            if pos == start:
                word = i.split()
                word = word[0]
                word = str(word)
                break
            pos += 1
    else:#если первоначальное слово задано, то строим текст начиная с него
        word = namespace.seed
    for i in range(len_text):#в цикле для i-го слова буем искать i + 1 при помощи полученой статистики
        text.append(word)
        word = find_next_word(word, dictionary_stat)#определяем подходящее слово
        if word == 'WRONG':#если подходящего слова нет, значит алгоритм защел в тупик
            return text
    return text


text = []#генерируемый текст
text = generate(namespace.length)#генерируем текст
if namespace.output != None:#если указано в какой файл записать сгенерируемый текст, то запишем его туда
    file = open(namespace.output, 'w')#указанный файл
    for i in text:#запись в файл
        file.write(str(i) + ' ')
    file.close()
else:#если не указано в какой файл записать сгенерируемый текст, то выведем его
    print(' '.join(text))