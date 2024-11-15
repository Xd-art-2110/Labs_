# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"

def task(filepath) -> None:  # TODO считать содержимое csv файла
    table = []
    with open(filepath) as f:
        lines = [line for line in csv.DictReader(f)]
        for line in lines[:5]:
            table.append(line)
    return json.dumps(table[:5], indent=4) # TODO Сериализовать в файл с отступами равными 4

print(task(INPUT_FILENAME), end = '')
