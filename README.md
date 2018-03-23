# python
Тексты должны лежать в папке texts.

********************************

Пример запросов в терминале: 

Обучение
=====================
>Консольный интерфейс:
>
>Обязательные поля: 
>
>`--input-dir` путь к директории, в которой лежит коллекция документов.
>
>`--model`  путь к файлу, в который сохраняется модель.
>
>Необязательные поля: 
>
>`--lc` приводить тексты к lowercase.
### Обычный запрос:
    python3 train.py --input-dir /Users/dmitrijpavlov/Desktop/Review/texts --model /Users/dmitrijpavlov/Desktop/Review/write.txt

### Запрос с преыедением всех слов к lowercase
    python3 train.py --input-dir /Users/dmitrijpavlov/Desktop/Review/texts --lc --model /Users/dmitrijpavlov/Desktop/Review/write.txt


Генератор
=====================
>Консольный интерфейс:
>
>Обязательные поля: 
>
>`--length` длина генерируемой последовательности.
>
>`--model` путь к файлу, из которого загружается модель.
>
>Необязательные поля: 
>
>`--seed` начальное слово. Если не указано, выбираем слово случайно из всех слов.
>
>`--output` файл, в который будет записан результат. Если аргумент отсутствует, выводится в stdout.
### Запрос с выводом в терминале:
    python3 generate.py --length 50 --model /Users/dmitrijpavlov/Desktop/Review/write.txt
    
### Запрос с выводом в указанном файле:
    python3 generate.py --length 50 --model /Users/dmitrijpavlov/Desktop/Review/write.txt --output /Users/dmitrijpavlov/Desktop/Review/name.txt

### Запрос с определенным первым словом:
    python3 generate.py --length 50 --model /Users/dmitrijpavlov/Desktop/Review/write.txt --seed можно
