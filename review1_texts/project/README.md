# python
********************************

Как пользоваться:

train.py
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

generate.py
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
