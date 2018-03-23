# python
Тексты должны лежать в папке texts

Пример запросов в терминале: 

Генератор:

python3 generate.py --length 50 --model /Users/dmitrijpavlov/Desktop/Review/write.txt

python3 generate.py --length 50 --model /Users/dmitrijpavlov/Desktop/Review/write.txt --output /Users/dmitrijpavlov/Desktop/Review/tryaaaa.txt

Траин:

python3 train.py --input-dir /Users/dmitrijpavlov/Desktop/Review/texts --lc --model /Users/dmitrijpavlov/Desktop/Review/write.txt
