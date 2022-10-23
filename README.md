## Sync folders

### TODO

[X] положить содержимое папок в 2 массива

[X] проитерировать по каждому из списков.
Если в списке А имеется файл, которого нет в списке В, то скопировать этот файл в папку В.
Если контрольная сумма файла списка В отличается от контрольной суммы списка А, то заменить это файлом списка А.

[x] логирование в файл

[x] добавить запуск через аргументы

[ ] периодический запуск


### HowTo

Written for __Python 3.7.4__

```commandline
% python3 main.py --help
usage: main.py [-h] --source SOURCE --replica REPLICA

Script to sync folders.

optional arguments:
  -h, --help         show this help message and exit
  --source SOURCE
  --replica REPLICA

```

```python
% python3 main.py --source source --replica replica
```
