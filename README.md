# python
Тексты должны лежать в папке texts.

********************************

Пример запросов в терминале: 

Обучение
=====================
>Обязательные поля в консольном интерфейсе: 
>
>`--input-dir` 
>
>`--model`
>
>Не обязательные поля в консольном интерфейсе: 
>
>`--lc`
### Обычный запрос:
    python3 train.py --input-dir /Users/dmitrijpavlov/Desktop/Review/texts --model /Users/dmitrijpavlov/Desktop/Review/write.txt

### Запрос с преыедением всех слов к lowercase
    python3 train.py --input-dir /Users/dmitrijpavlov/Desktop/Review/texts --lc --model /Users/dmitrijpavlov/Desktop/Review/write.txt


Генератор
=====================
>Обязательные поля в консольном интерфейсе: 
>
>`--length` 
>
>`--model`
>
>Не обязательные поля в консольном интерфейсе: 
>
>`--seed`
>
>`--output`
### Запрос с выводом в терминале:
    python3 generate.py --length 50 --model /Users/dmitrijpavlov/Desktop/Review/write.txt
    
### Запрос с выводом в указанном файле:
    python3 generate.py --length 50 --model /Users/dmitrijpavlov/Desktop/Review/write.txt --output /Users/dmitrijpavlov/Desktop/Review/name.txt

### Запрос с определенным первым словом:
    python3 generate.py --length 50 --model /Users/dmitrijpavlov/Desktop/Review/write.txt --seed можно
